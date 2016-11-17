# coding: utf-8

"""
    RiseML API


    OpenAPI spec version: 1.1.0
    Contact: support@riseml.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class User(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, username=None, email=None, api_key=None, ssh_key=None, fingerprint=None):
        """
        User - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'username': 'str',
            'email': 'str',
            'api_key': 'str',
            'ssh_key': 'str',
            'fingerprint': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'username': 'username',
            'email': 'email',
            'api_key': 'api_key',
            'ssh_key': 'ssh_key',
            'fingerprint': 'fingerprint'
        }

        self._id = id
        self._username = username
        self._email = email
        self._api_key = api_key
        self._ssh_key = ssh_key
        self._fingerprint = fingerprint


    @property
    def id(self):
        """
        Gets the id of this User.


        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.


        :param id: The id of this User.
        :type: str
        """

        self._id = id

    @property
    def username(self):
        """
        Gets the username of this User.


        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this User.


        :param username: The username of this User.
        :type: str
        """

        self._username = username

    @property
    def email(self):
        """
        Gets the email of this User.


        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this User.


        :param email: The email of this User.
        :type: str
        """

        self._email = email

    @property
    def api_key(self):
        """
        Gets the api_key of this User.


        :return: The api_key of this User.
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """
        Sets the api_key of this User.


        :param api_key: The api_key of this User.
        :type: str
        """

        self._api_key = api_key

    @property
    def ssh_key(self):
        """
        Gets the ssh_key of this User.


        :return: The ssh_key of this User.
        :rtype: str
        """
        return self._ssh_key

    @ssh_key.setter
    def ssh_key(self, ssh_key):
        """
        Sets the ssh_key of this User.


        :param ssh_key: The ssh_key of this User.
        :type: str
        """

        self._ssh_key = ssh_key

    @property
    def fingerprint(self):
        """
        Gets the fingerprint of this User.


        :return: The fingerprint of this User.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """
        Sets the fingerprint of this User.


        :param fingerprint: The fingerprint of this User.
        :type: str
        """

        self._fingerprint = fingerprint

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
