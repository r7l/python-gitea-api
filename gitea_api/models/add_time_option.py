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

class AddTimeOption(object):
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
        'created': 'datetime',
        'time': 'int',
        'user_name': 'str'
    }

    attribute_map = {
        'created': 'created',
        'time': 'time',
        'user_name': 'user_name'
    }

    def __init__(self, created=None, time=None, user_name=None):  # noqa: E501
        """AddTimeOption - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._time = None
        self._user_name = None
        self.discriminator = None
        if created is not None:
            self.created = created
        self.time = time
        if user_name is not None:
            self.user_name = user_name

    @property
    def created(self):
        """Gets the created of this AddTimeOption.  # noqa: E501


        :return: The created of this AddTimeOption.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this AddTimeOption.


        :param created: The created of this AddTimeOption.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def time(self):
        """Gets the time of this AddTimeOption.  # noqa: E501

        time in seconds  # noqa: E501

        :return: The time of this AddTimeOption.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this AddTimeOption.

        time in seconds  # noqa: E501

        :param time: The time of this AddTimeOption.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def user_name(self):
        """Gets the user_name of this AddTimeOption.  # noqa: E501

        User who spent the time (optional)  # noqa: E501

        :return: The user_name of this AddTimeOption.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AddTimeOption.

        User who spent the time (optional)  # noqa: E501

        :param user_name: The user_name of this AddTimeOption.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if issubclass(AddTimeOption, dict):
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
        if not isinstance(other, AddTimeOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
