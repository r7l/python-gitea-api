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

class WikiPage(object):
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
        'commit_count': 'int',
        'content_base64': 'str',
        'footer': 'str',
        'html_url': 'str',
        'last_commit': 'WikiCommit',
        'sidebar': 'str',
        'sub_url': 'str',
        'title': 'str'
    }

    attribute_map = {
        'commit_count': 'commit_count',
        'content_base64': 'content_base64',
        'footer': 'footer',
        'html_url': 'html_url',
        'last_commit': 'last_commit',
        'sidebar': 'sidebar',
        'sub_url': 'sub_url',
        'title': 'title'
    }

    def __init__(self, commit_count=None, content_base64=None, footer=None, html_url=None, last_commit=None, sidebar=None, sub_url=None, title=None):  # noqa: E501
        """WikiPage - a model defined in Swagger"""  # noqa: E501
        self._commit_count = None
        self._content_base64 = None
        self._footer = None
        self._html_url = None
        self._last_commit = None
        self._sidebar = None
        self._sub_url = None
        self._title = None
        self.discriminator = None
        if commit_count is not None:
            self.commit_count = commit_count
        if content_base64 is not None:
            self.content_base64 = content_base64
        if footer is not None:
            self.footer = footer
        if html_url is not None:
            self.html_url = html_url
        if last_commit is not None:
            self.last_commit = last_commit
        if sidebar is not None:
            self.sidebar = sidebar
        if sub_url is not None:
            self.sub_url = sub_url
        if title is not None:
            self.title = title

    @property
    def commit_count(self):
        """Gets the commit_count of this WikiPage.  # noqa: E501


        :return: The commit_count of this WikiPage.  # noqa: E501
        :rtype: int
        """
        return self._commit_count

    @commit_count.setter
    def commit_count(self, commit_count):
        """Sets the commit_count of this WikiPage.


        :param commit_count: The commit_count of this WikiPage.  # noqa: E501
        :type: int
        """

        self._commit_count = commit_count

    @property
    def content_base64(self):
        """Gets the content_base64 of this WikiPage.  # noqa: E501

        Page content, base64 encoded  # noqa: E501

        :return: The content_base64 of this WikiPage.  # noqa: E501
        :rtype: str
        """
        return self._content_base64

    @content_base64.setter
    def content_base64(self, content_base64):
        """Sets the content_base64 of this WikiPage.

        Page content, base64 encoded  # noqa: E501

        :param content_base64: The content_base64 of this WikiPage.  # noqa: E501
        :type: str
        """

        self._content_base64 = content_base64

    @property
    def footer(self):
        """Gets the footer of this WikiPage.  # noqa: E501


        :return: The footer of this WikiPage.  # noqa: E501
        :rtype: str
        """
        return self._footer

    @footer.setter
    def footer(self, footer):
        """Sets the footer of this WikiPage.


        :param footer: The footer of this WikiPage.  # noqa: E501
        :type: str
        """

        self._footer = footer

    @property
    def html_url(self):
        """Gets the html_url of this WikiPage.  # noqa: E501


        :return: The html_url of this WikiPage.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this WikiPage.


        :param html_url: The html_url of this WikiPage.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def last_commit(self):
        """Gets the last_commit of this WikiPage.  # noqa: E501


        :return: The last_commit of this WikiPage.  # noqa: E501
        :rtype: WikiCommit
        """
        return self._last_commit

    @last_commit.setter
    def last_commit(self, last_commit):
        """Sets the last_commit of this WikiPage.


        :param last_commit: The last_commit of this WikiPage.  # noqa: E501
        :type: WikiCommit
        """

        self._last_commit = last_commit

    @property
    def sidebar(self):
        """Gets the sidebar of this WikiPage.  # noqa: E501


        :return: The sidebar of this WikiPage.  # noqa: E501
        :rtype: str
        """
        return self._sidebar

    @sidebar.setter
    def sidebar(self, sidebar):
        """Sets the sidebar of this WikiPage.


        :param sidebar: The sidebar of this WikiPage.  # noqa: E501
        :type: str
        """

        self._sidebar = sidebar

    @property
    def sub_url(self):
        """Gets the sub_url of this WikiPage.  # noqa: E501


        :return: The sub_url of this WikiPage.  # noqa: E501
        :rtype: str
        """
        return self._sub_url

    @sub_url.setter
    def sub_url(self, sub_url):
        """Sets the sub_url of this WikiPage.


        :param sub_url: The sub_url of this WikiPage.  # noqa: E501
        :type: str
        """

        self._sub_url = sub_url

    @property
    def title(self):
        """Gets the title of this WikiPage.  # noqa: E501


        :return: The title of this WikiPage.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this WikiPage.


        :param title: The title of this WikiPage.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(WikiPage, dict):
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
        if not isinstance(other, WikiPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
