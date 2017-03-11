# coding: utf-8

"""
    RiseML API


    OpenAPI spec version: 1.1.0
    Contact: contact@riseml.com
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
    def __init__(self, id=None, username=None, email=None, api_key_plaintext=None, github_access_token=None, is_admin=None, is_enabled=None, github_id=None):
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
            'api_key_plaintext': 'str',
            'github_access_token': 'str',
            'is_admin': 'bool',
            'is_enabled': 'bool',
            'github_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'username': 'username',
            'email': 'email',
            'api_key_plaintext': 'api_key_plaintext',
            'github_access_token': 'github_access_token',
            'is_admin': 'is_admin',
            'is_enabled': 'is_enabled',
            'github_id': 'github_id'
        }

        self._id = id
        self._username = username
        self._email = email
        self._api_key_plaintext = api_key_plaintext
        self._github_access_token = github_access_token
        self._is_admin = is_admin
        self._is_enabled = is_enabled
        self._github_id = github_id


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
    def api_key_plaintext(self):
        """
        Gets the api_key_plaintext of this User.


        :return: The api_key_plaintext of this User.
        :rtype: str
        """
        return self._api_key_plaintext

    @api_key_plaintext.setter
    def api_key_plaintext(self, api_key_plaintext):
        """
        Sets the api_key_plaintext of this User.


        :param api_key_plaintext: The api_key_plaintext of this User.
        :type: str
        """

        self._api_key_plaintext = api_key_plaintext

    @property
    def github_access_token(self):
        """
        Gets the github_access_token of this User.


        :return: The github_access_token of this User.
        :rtype: str
        """
        return self._github_access_token

    @github_access_token.setter
    def github_access_token(self, github_access_token):
        """
        Sets the github_access_token of this User.


        :param github_access_token: The github_access_token of this User.
        :type: str
        """

        self._github_access_token = github_access_token

    @property
    def is_admin(self):
        """
        Gets the is_admin of this User.


        :return: The is_admin of this User.
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """
        Sets the is_admin of this User.


        :param is_admin: The is_admin of this User.
        :type: bool
        """

        self._is_admin = is_admin

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this User.


        :return: The is_enabled of this User.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this User.


        :param is_enabled: The is_enabled of this User.
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def github_id(self):
        """
        Gets the github_id of this User.


        :return: The github_id of this User.
        :rtype: int
        """
        return self._github_id

    @github_id.setter
    def github_id(self, github_id):
        """
        Sets the github_id of this User.


        :param github_id: The github_id of this User.
        :type: int
        """

        self._github_id = github_id

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
