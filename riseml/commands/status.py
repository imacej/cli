# -*- coding: utf-8 -*-

from __future__ import print_function

import json

from riseml.client import DefaultApi, ApiClient
from riseml import util
from riseml.errors import handle_error


def add_status_parser(subparsers):
    parser = subparsers.add_parser('status', help="show (running) experiments")
    parser.add_argument('id', help='id of RiseML entity for which to show status', nargs='?')
    parser.add_argument('-a', '--all', help="show all experiments", action="store_const", const=True)
    parser.add_argument('-n', '--num-last', help="show n last experiments, 0 for all", default=10, type=int)
    parser.add_argument('-u', '--all-users', help="show experiments for all users (admin only)", action="store_const", const=True)
    parser.add_argument('-l', '--long', help="expand series", action="store_const", const=True)
    parser.set_defaults(run=run)


def run(args):
    api_client = ApiClient()
    client = DefaultApi(api_client)

    if args.id and util.is_experiment_id(args.id):
        experiment = util.call_api(
            lambda: client.get_experiment(args.id),
            not_found=lambda: handle_error("Could not find experiment!")
        )
        if experiment.children:
            show_experiment_group(experiment)
        else:
            show_experiment(experiment)
    elif args.id and util.is_job_id(args.id):
        job = util.call_api(
            lambda: client.get_job(args.id),
            not_found=lambda: handle_error("Could not find job!")
        )
        show_job(job)
    elif args.id and util.is_user_id(args.id):
        query_args = {'user': args.id[1:]}
        if not args.all:
            query_args['states'] = 'CREATED|PENDING|STARTING|BUILDING|RUNNING'
        else:
            query_args['count'] = args.num_last
        experiments = util.call_api(lambda: client.get_experiments(**query_args))
        show_experiments(experiments, all=args.all, collapsed=not args.long)
    elif not args.id:
        query_args = {'all_users': args.all_users}
        if not args.all:
            query_args['states'] = 'CREATED|PENDING|STARTING|BUILDING|RUNNING'
        else:
            query_args['count'] = args.num_last
        experiments = util.call_api(lambda: client.get_experiments(**query_args))
        show_experiments(experiments, all=args.all, collapsed=not args.long, users=args.all_users)
    else:
        handle_error("Id does not identify any RiseML entity!")


def params(experiment):
    return ', '.join(['{}={}'.format(p, v) for p, v in sorted(json.loads(experiment.params).items())])


def format_value(v):
    try:
       f = float(v)
       return '%.5G' % f
    except ValueError:
       return str(v)


def result(experiment):
    if experiment.result:
        return ', '.join(['{}={}'.format(p, format_value(v))
                          for p, v in sorted(json.loads(experiment.result).items())])
    return ''


def show_dict(dictionary, indentation=2, title=None):
    if not dictionary:
        return
    if title:
        print(title)
    whitespaces = ' ' * indentation
    for attribute, value in dictionary.items():
        if isinstance(value, dict):
            print("{}{}:".format(whitespaces, attribute))
            show_dict(value, indentation=indentation + 2)
        elif value is not None:
            print("{}{}: {}".format(whitespaces, attribute, value))


def show_common_header(entity, type):
    print("ID: {}".format(entity.short_id))
    print("Type: {}".format(type))
    print("State: {}{}".format(util.get_state_symbol(entity.state),
                               entity.state))
    show_timing(entity.started_at, entity.finished_at)


def show_job_table(jobs):
    rows = [
        ([job.short_id,
         '%s%s' % (util.get_state_symbol(job.state), job.state),
         util.get_since_str(job.started_at),
         util.str_duration(job.started_at, job.finished_at, is_millis=True),
         job.reason or '',
         job.message[:17] + '...' if job.message and len(job.message) > 20 else job.message or '',
         job.exit_code if job.exit_code is not None else '',
         '%d' % job.gpus, '%.1f' % job.cpus, '%d' % job.mem]) for job in jobs
    ]

    util.print_table(
        header=['JOB ID', 'STATE', 'STARTED', 'DURATION', 'REASON', 'MESSAGE', 'EXIT CODE', 'GPU', 'CPU', 'MEM'],
        min_widths=[13, 11, 8, 9, 13, 20, 10, 6, 6, 6],
        rows=rows
    )


def show_timing(started_at, finished_at):
    if started_at:
        print("Started:  {}".format(util.str_timestamp(started_at / 1000)))
        if finished_at is not None:
            print("Finished: {}".format(util.str_timestamp(finished_at / 1000)))
        print("Duration: {}".format(util.str_duration(started_at,
                                                    finished_at, is_millis=True)))


def show_experiment(experiment):
    show_common_header(experiment, "Experiment")
    print("Image: {}".format(experiment.image))
    print("Framework: {}".format(experiment.framework))
    show_dict(experiment.framework_config, title="Framework Config:")

    if util.has_tensorboard(experiment):
        tensorboard_job = util.tensorboard_job(experiment)
        if tensorboard_job:
            if tensorboard_job.state in ['RUNNING']:
                print("Tensorboard: {}".format(util.tensorboard_job_url(tensorboard_job)))
            else:
                print("Tensorboard: OFFLINE")

    print("Run Commands:")
    print(''.join(["  {}".format(command) for command in experiment.run_commands]))
    print("Concurrency: {}".format(experiment.concurrency))
    print("Parameters: {}".format(params(experiment)))
    print("Result: {}\n".format(result(experiment)))

    show_job_table(experiment.jobs)


def show_job(job):
    show_common_header(job, "Job")
    if job.reason is not None:
        print("Reason: {}".format(job.reason))
    if job.message is not None:
        print("Message: {}".format(job.message))
    if job.exit_code is not None:
        print("Exit Code: {}".format(job.exit_code))
    print("Requested cpus: {}".format(job.cpus))
    print("Requested mem: {}".format(job.mem))
    print("Requested gpus: {}".format(job.gpus))
    print("Run Commands:")
    if json.loads(job.commands):
        print(''.join(["  {}".format(command) for command in json.loads(job.commands)]))
    show_dict(json.loads(job.environment), title="Environment:")
    if job.state == 'FAILED':
        print("Reason: {}".format(job.reason))


def get_experiments_rows(group, with_project=True, with_type=True, with_params=True,
                         with_user=False, indent=True, with_result=True, use_started_at=False,
                         with_duration=False):
    rows = []

    for i, experiment in enumerate(group.children):
        indent_str = (u'├╴' if i < len(group.children) - 1 else u'╰╴') if indent else ''
        values = [indent_str + experiment.short_id]

        if with_user:
            values += [group.user.username]

        if with_project:
            values += [group.project.name]

        values += [u'%s%s' % (util.get_state_symbol(experiment.state), experiment.state)]

        if use_started_at:
            values += [util.get_since_str(experiment.started_at)]
        else:
            values += [util.get_since_str(experiment.created_at)]

        if with_duration:
            values += [util.str_duration(experiment.started_at, experiment.finished_at,
                                         is_millis=True)]

        if with_type:
            values += [indent_str + 'Experiment']
        if with_params:
            values += [params(experiment)]
        if with_result:
            values += [result(experiment)]

        rows.append(values)

    return rows


def show_experiment_group(group):
    show_common_header(group, 'Set')

    if group.framework == 'tensorflow' and group.framework_config.get('tensorboard', False):
        tensorboard_job = next(job for job in group.jobs if job.role == 'tensorboard')
        if tensorboard_job.state in ['RUNNING']:
            print("Tensorboard: {}".format(util.tensorboard_job_url(tensorboard_job)))
        else:
            print("Tensorboard: OFFLINE")

    print()
    util.print_table(
        header=['EXP ID', 'STATE', 'STARTED', 'DURATION', 'PARAMS', 'RESULT'],
        min_widths=(6, 9, 11, 9, 14, 14),
        rows=get_experiments_rows(group, with_project=False, with_type=False, indent=False,
                                  use_started_at=True, with_duration=True)
    )

    if group.jobs:
        print()
        show_job_table(group.jobs)


def show_experiments(experiments, all=False, collapsed=True, users=False):
    headers, widths = _get_status_headers(collapsed, users)
    rows = _get_experiment_rows(experiments, all, collapsed, users)
    util.print_table(
        header=headers,
        min_widths=widths,
        rows=rows
    )

def _get_status_headers(collapsed=False, users=False):
    header = ['ID', 'PROJECT', 'STATE', 'AGE', 'TYPE']
    widths = (6, 14, 10, 11, 15)
    if users:
        header = ['ID', 'USER', 'PROJECT', 'STATE', 'AGE', 'TYPE']
        widths = (6, 6, 14, 10, 11, 15)
    if not collapsed:
        header += ['PARAMS' , 'RESULT']
        widths += (14, 14)
    return header, widths


def _get_experiment_rows(experiments, all=False, collapsed=True, users=False):
    rows = []
    for experiment in experiments:
        if not all and experiment.state in ['FINISHED', 'KILLED', 'FAILED']:
            continue

        values = [experiment.short_id]
        if users:
            values += [experiment.user.username]
        values += [
            experiment.project.name,
            '%s%s' % (util.get_state_symbol(experiment.state), experiment.state),
            util.get_since_str(experiment.created_at),
            experiment.type
        ]

        if not collapsed:
            values += ['', result(experiment)]

        rows.append(values)

        if not collapsed and experiment.children:
            rows += get_experiments_rows(experiment, with_user=users)

    return rows