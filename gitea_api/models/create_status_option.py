# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.18.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreateStatusOption(object):
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
        'context': 'str',
        'description': 'str',
        'state': 'CommitStatusState',
        'target_url': 'str'
    }

    attribute_map = {
        'context': 'context',
        'description': 'description',
        'state': 'state',
        'target_url': 'target_url'
    }

    def __init__(self, context=None, description=None, state=None, target_url=None):  # noqa: E501
        """CreateStatusOption - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._description = None
        self._state = None
        self._target_url = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if description is not None:
            self.description = description
        if state is not None:
            self.state = state
        if target_url is not None:
            self.target_url = target_url

    @property
    def context(self):
        """Gets the context of this CreateStatusOption.  # noqa: E501


        :return: The context of this CreateStatusOption.  # noqa: E501
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this CreateStatusOption.


        :param context: The context of this CreateStatusOption.  # noqa: E501
        :type: str
        """

        self._context = context

    @property
    def description(self):
        """Gets the description of this CreateStatusOption.  # noqa: E501


        :return: The description of this CreateStatusOption.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateStatusOption.


        :param description: The description of this CreateStatusOption.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def state(self):
        """Gets the state of this CreateStatusOption.  # noqa: E501


        :return: The state of this CreateStatusOption.  # noqa: E501
        :rtype: CommitStatusState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CreateStatusOption.


        :param state: The state of this CreateStatusOption.  # noqa: E501
        :type: CommitStatusState
        """

        self._state = state

    @property
    def target_url(self):
        """Gets the target_url of this CreateStatusOption.  # noqa: E501


        :return: The target_url of this CreateStatusOption.  # noqa: E501
        :rtype: str
        """
        return self._target_url

    @target_url.setter
    def target_url(self, target_url):
        """Sets the target_url of this CreateStatusOption.


        :param target_url: The target_url of this CreateStatusOption.  # noqa: E501
        :type: str
        """

        self._target_url = target_url

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
        if issubclass(CreateStatusOption, dict):
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
        if not isinstance(other, CreateStatusOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
