# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.17.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GitHook(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'content': 'str',
        'is_active': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'content': 'content',
        'is_active': 'is_active',
        'name': 'name'
    }

    def __init__(self, content=None, is_active=None, name=None):  # noqa: E501
        """GitHook - a model defined in Swagger"""  # noqa: E501
        self._content = None
        self._is_active = None
        self._name = None
        self.discriminator = None
        if content is not None:
            self.content = content
        if is_active is not None:
            self.is_active = is_active
        if name is not None:
            self.name = name

    @property
    def content(self):
        """Gets the content of this GitHook.  # noqa: E501


        :return: The content of this GitHook.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this GitHook.


        :param content: The content of this GitHook.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def is_active(self):
        """Gets the is_active of this GitHook.  # noqa: E501


        :return: The is_active of this GitHook.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this GitHook.


        :param is_active: The is_active of this GitHook.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def name(self):
        """Gets the name of this GitHook.  # noqa: E501


        :return: The name of this GitHook.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GitHook.


        :param name: The name of this GitHook.  # noqa: E501
        :type: str
        """

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(GitHook, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GitHook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
