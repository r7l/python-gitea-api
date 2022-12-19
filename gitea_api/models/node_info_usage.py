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

class NodeInfoUsage(object):
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
        'local_comments': 'int',
        'local_posts': 'int',
        'users': 'NodeInfoUsageUsers'
    }

    attribute_map = {
        'local_comments': 'localComments',
        'local_posts': 'localPosts',
        'users': 'users'
    }

    def __init__(self, local_comments=None, local_posts=None, users=None):  # noqa: E501
        """NodeInfoUsage - a model defined in Swagger"""  # noqa: E501
        self._local_comments = None
        self._local_posts = None
        self._users = None
        self.discriminator = None
        if local_comments is not None:
            self.local_comments = local_comments
        if local_posts is not None:
            self.local_posts = local_posts
        if users is not None:
            self.users = users

    @property
    def local_comments(self):
        """Gets the local_comments of this NodeInfoUsage.  # noqa: E501


        :return: The local_comments of this NodeInfoUsage.  # noqa: E501
        :rtype: int
        """
        return self._local_comments

    @local_comments.setter
    def local_comments(self, local_comments):
        """Sets the local_comments of this NodeInfoUsage.


        :param local_comments: The local_comments of this NodeInfoUsage.  # noqa: E501
        :type: int
        """

        self._local_comments = local_comments

    @property
    def local_posts(self):
        """Gets the local_posts of this NodeInfoUsage.  # noqa: E501


        :return: The local_posts of this NodeInfoUsage.  # noqa: E501
        :rtype: int
        """
        return self._local_posts

    @local_posts.setter
    def local_posts(self, local_posts):
        """Sets the local_posts of this NodeInfoUsage.


        :param local_posts: The local_posts of this NodeInfoUsage.  # noqa: E501
        :type: int
        """

        self._local_posts = local_posts

    @property
    def users(self):
        """Gets the users of this NodeInfoUsage.  # noqa: E501


        :return: The users of this NodeInfoUsage.  # noqa: E501
        :rtype: NodeInfoUsageUsers
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this NodeInfoUsage.


        :param users: The users of this NodeInfoUsage.  # noqa: E501
        :type: NodeInfoUsageUsers
        """

        self._users = users

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
        if issubclass(NodeInfoUsage, dict):
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
        if not isinstance(other, NodeInfoUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
