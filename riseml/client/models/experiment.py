# coding: utf-8

"""
    RiseML API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.1.0
    Contact: contact@riseml.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class Experiment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, short_id=None, state=None, state_changed_at=None, created_at=None, started_at=None, finished_at=None, framework=None, framework_config=None, image=None, run_commands=None, concurrency=None, params=None, type=None, jobs=None, changeset=None, user=None, children=None):
        """
        Experiment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'short_id': 'str',
            'state': 'str',
            'state_changed_at': 'int',
            'created_at': 'int',
            'started_at': 'int',
            'finished_at': 'int',
            'framework': 'str',
            'framework_config': 'object',
            'image': 'str',
            'run_commands': 'list[str]',
            'concurrency': 'int',
            'params': 'str',
            'type': 'str',
            'jobs': 'list[Job]',
            'changeset': 'Changeset',
            'user': 'User',
            'children': 'list[Experiment]'
        }

        self.attribute_map = {
            'id': 'id',
            'short_id': 'short_id',
            'state': 'state',
            'state_changed_at': 'state_changed_at',
            'created_at': 'created_at',
            'started_at': 'started_at',
            'finished_at': 'finished_at',
            'framework': 'framework',
            'framework_config': 'framework_config',
            'image': 'image',
            'run_commands': 'run_commands',
            'concurrency': 'concurrency',
            'params': 'params',
            'type': 'type',
            'jobs': 'jobs',
            'changeset': 'changeset',
            'user': 'user',
            'children': 'children'
        }

        self._id = id
        self._short_id = short_id
        self._state = state
        self._state_changed_at = state_changed_at
        self._created_at = created_at
        self._started_at = started_at
        self._finished_at = finished_at
        self._framework = framework
        self._framework_config = framework_config
        self._image = image
        self._run_commands = run_commands
        self._concurrency = concurrency
        self._params = params
        self._type = type
        self._jobs = jobs
        self._changeset = changeset
        self._user = user
        self._children = children


    @property
    def id(self):
        """
        Gets the id of this Experiment.


        :return: The id of this Experiment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Experiment.


        :param id: The id of this Experiment.
        :type: str
        """

        self._id = id

    @property
    def short_id(self):
        """
        Gets the short_id of this Experiment.


        :return: The short_id of this Experiment.
        :rtype: str
        """
        return self._short_id

    @short_id.setter
    def short_id(self, short_id):
        """
        Sets the short_id of this Experiment.


        :param short_id: The short_id of this Experiment.
        :type: str
        """

        self._short_id = short_id

    @property
    def state(self):
        """
        Gets the state of this Experiment.


        :return: The state of this Experiment.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Experiment.


        :param state: The state of this Experiment.
        :type: str
        """

        self._state = state

    @property
    def state_changed_at(self):
        """
        Gets the state_changed_at of this Experiment.


        :return: The state_changed_at of this Experiment.
        :rtype: int
        """
        return self._state_changed_at

    @state_changed_at.setter
    def state_changed_at(self, state_changed_at):
        """
        Sets the state_changed_at of this Experiment.


        :param state_changed_at: The state_changed_at of this Experiment.
        :type: int
        """

        self._state_changed_at = state_changed_at

    @property
    def created_at(self):
        """
        Gets the created_at of this Experiment.


        :return: The created_at of this Experiment.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Experiment.


        :param created_at: The created_at of this Experiment.
        :type: int
        """

        self._created_at = created_at

    @property
    def started_at(self):
        """
        Gets the started_at of this Experiment.


        :return: The started_at of this Experiment.
        :rtype: int
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """
        Sets the started_at of this Experiment.


        :param started_at: The started_at of this Experiment.
        :type: int
        """

        self._started_at = started_at

    @property
    def finished_at(self):
        """
        Gets the finished_at of this Experiment.


        :return: The finished_at of this Experiment.
        :rtype: int
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """
        Sets the finished_at of this Experiment.


        :param finished_at: The finished_at of this Experiment.
        :type: int
        """

        self._finished_at = finished_at

    @property
    def framework(self):
        """
        Gets the framework of this Experiment.


        :return: The framework of this Experiment.
        :rtype: str
        """
        return self._framework

    @framework.setter
    def framework(self, framework):
        """
        Sets the framework of this Experiment.


        :param framework: The framework of this Experiment.
        :type: str
        """

        self._framework = framework

    @property
    def framework_config(self):
        """
        Gets the framework_config of this Experiment.


        :return: The framework_config of this Experiment.
        :rtype: object
        """
        return self._framework_config

    @framework_config.setter
    def framework_config(self, framework_config):
        """
        Sets the framework_config of this Experiment.


        :param framework_config: The framework_config of this Experiment.
        :type: object
        """

        self._framework_config = framework_config

    @property
    def image(self):
        """
        Gets the image of this Experiment.


        :return: The image of this Experiment.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this Experiment.


        :param image: The image of this Experiment.
        :type: str
        """

        self._image = image

    @property
    def run_commands(self):
        """
        Gets the run_commands of this Experiment.


        :return: The run_commands of this Experiment.
        :rtype: list[str]
        """
        return self._run_commands

    @run_commands.setter
    def run_commands(self, run_commands):
        """
        Sets the run_commands of this Experiment.


        :param run_commands: The run_commands of this Experiment.
        :type: list[str]
        """

        self._run_commands = run_commands

    @property
    def concurrency(self):
        """
        Gets the concurrency of this Experiment.


        :return: The concurrency of this Experiment.
        :rtype: int
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        """
        Sets the concurrency of this Experiment.


        :param concurrency: The concurrency of this Experiment.
        :type: int
        """

        self._concurrency = concurrency

    @property
    def params(self):
        """
        Gets the params of this Experiment.


        :return: The params of this Experiment.
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        """
        Sets the params of this Experiment.


        :param params: The params of this Experiment.
        :type: str
        """

        self._params = params

    @property
    def type(self):
        """
        Gets the type of this Experiment.


        :return: The type of this Experiment.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Experiment.


        :param type: The type of this Experiment.
        :type: str
        """

        self._type = type

    @property
    def jobs(self):
        """
        Gets the jobs of this Experiment.


        :return: The jobs of this Experiment.
        :rtype: list[Job]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """
        Sets the jobs of this Experiment.


        :param jobs: The jobs of this Experiment.
        :type: list[Job]
        """

        self._jobs = jobs

    @property
    def changeset(self):
        """
        Gets the changeset of this Experiment.


        :return: The changeset of this Experiment.
        :rtype: Changeset
        """
        return self._changeset

    @changeset.setter
    def changeset(self, changeset):
        """
        Sets the changeset of this Experiment.


        :param changeset: The changeset of this Experiment.
        :type: Changeset
        """

        self._changeset = changeset

    @property
    def user(self):
        """
        Gets the user of this Experiment.


        :return: The user of this Experiment.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this Experiment.


        :param user: The user of this Experiment.
        :type: User
        """

        self._user = user

    @property
    def children(self):
        """
        Gets the children of this Experiment.


        :return: The children of this Experiment.
        :rtype: list[Experiment]
        """
        return self._children

    @children.setter
    def children(self, children):
        """
        Sets the children of this Experiment.


        :param children: The children of this Experiment.
        :type: list[Experiment]
        """

        self._children = children

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
