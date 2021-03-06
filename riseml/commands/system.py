from riseml.client import AdminApi, ApiClient
from riseml.util import call_api
from .system_info import add_system_info_parser
from .system_test import add_system_test_parser

def add_system_parser(subparsers):
    parser = subparsers.add_parser('system', help="system level commands")
    subsubparsers = parser.add_subparsers()
    add_system_info_parser(subsubparsers)
    add_system_test_parser(subsubparsers)
    def run(args):
        parser.print_usage()
    parser.set_defaults(run=run)

