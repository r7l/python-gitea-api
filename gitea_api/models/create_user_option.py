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

class CreateUserOption(object):
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
        'email': 'str',
        'full_name': 'str',
        'login_name': 'str',
        'must_change_password': 'bool',
        'password': 'str',
        'restricted': 'bool',
        'send_notify': 'bool',
        'source_id': 'int',
        'username': 'str',
        'visibility': 'str'
    }

    attribute_map = {
        'email': 'email',
        'full_name': 'full_name',
        'login_name': 'login_name',
        'must_change_password': 'must_change_password',
        'password': 'password',
        'restricted': 'restricted',
        'send_notify': 'send_notify',
        'source_id': 'source_id',
        'username': 'username',
        'visibility': 'visibility'
    }

    def __init__(self, email=None, full_name=None, login_name=None, must_change_password=None, password=None, restricted=None, send_notify=None, source_id=None, username=None, visibility=None):  # noqa: E501
        """CreateUserOption - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._full_name = None
        self._login_name = None
        self._must_change_password = None
        self._password = None
        self._restricted = None
        self._send_notify = None
        self._source_id = None
        self._username = None
        self._visibility = None
        self.discriminator = None
        self.email = email
        if full_name is not None:
            self.full_name = full_name
        if login_name is not None:
            self.login_name = login_name
        if must_change_password is not None:
            self.must_change_password = must_change_password
        self.password = password
        if restricted is not None:
            self.restricted = restricted
        if send_notify is not None:
            self.send_notify = send_notify
        if source_id is not None:
            self.source_id = source_id
        self.username = username
        if visibility is not None:
            self.visibility = visibility

    @property
    def email(self):
        """Gets the email of this CreateUserOption.  # noqa: E501


        :return: The email of this CreateUserOption.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateUserOption.


        :param email: The email of this CreateUserOption.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def full_name(self):
        """Gets the full_name of this CreateUserOption.  # noqa: E501


        :return: The full_name of this CreateUserOption.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this CreateUserOption.


        :param full_name: The full_name of this CreateUserOption.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def login_name(self):
        """Gets the login_name of this CreateUserOption.  # noqa: E501


        :return: The login_name of this CreateUserOption.  # noqa: E501
        :rtype: str
        """
        return self._login_name

    @login_name.setter
    def login_name(self, login_name):
        """Sets the login_name of this CreateUserOption.


        :param login_name: The login_name of this CreateUserOption.  # noqa: E501
        :type: str
        """

        self._login_name = login_name

    @property
    def must_change_password(self):
        """Gets the must_change_password of this CreateUserOption.  # noqa: E501


        :return: The must_change_password of this CreateUserOption.  # noqa: E501
        :rtype: bool
        """
        return self._must_change_password

    @must_change_password.setter
    def must_change_password(self, must_change_password):
        """Sets the must_change_password of this CreateUserOption.


        :param must_change_password: The must_change_password of this CreateUserOption.  # noqa: E501
        :type: bool
        """

        self._must_change_password = must_change_password

    @property
    def password(self):
        """Gets the password of this CreateUserOption.  # noqa: E501


        :return: The password of this CreateUserOption.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateUserOption.


        :param password: The password of this CreateUserOption.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def restricted(self):
        """Gets the restricted of this CreateUserOption.  # noqa: E501


        :return: The restricted of this CreateUserOption.  # noqa: E501
        :rtype: bool
        """
        return self._restricted

    @restricted.setter
    def restricted(self, restricted):
        """Sets the restricted of this CreateUserOption.


        :param restricted: The restricted of this CreateUserOption.  # noqa: E501
        :type: bool
        """

        self._restricted = restricted

    @property
    def send_notify(self):
        """Gets the send_notify of this CreateUserOption.  # noqa: E501


        :return: The send_notify of this CreateUserOption.  # noqa: E501
        :rtype: bool
        """
        return self._send_notify

    @send_notify.setter
    def send_notify(self, send_notify):
        """Sets the send_notify of this CreateUserOption.


        :param send_notify: The send_notify of this CreateUserOption.  # noqa: E501
        :type: bool
        """

        self._send_notify = send_notify

    @property
    def source_id(self):
        """Gets the source_id of this CreateUserOption.  # noqa: E501


        :return: The source_id of this CreateUserOption.  # noqa: E501
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this CreateUserOption.


        :param source_id: The source_id of this CreateUserOption.  # noqa: E501
        :type: int
        """

        self._source_id = source_id

    @property
    def username(self):
        """Gets the username of this CreateUserOption.  # noqa: E501


        :return: The username of this CreateUserOption.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CreateUserOption.


        :param username: The username of this CreateUserOption.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def visibility(self):
        """Gets the visibility of this CreateUserOption.  # noqa: E501


        :return: The visibility of this CreateUserOption.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this CreateUserOption.


        :param visibility: The visibility of this CreateUserOption.  # noqa: E501
        :type: str
        """

        self._visibility = visibility

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
        if issubclass(CreateUserOption, dict):
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
        if not isinstance(other, CreateUserOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
