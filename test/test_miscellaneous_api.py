# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.18.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import gitea_api
from gitea_api.api.miscellaneous_api import MiscellaneousApi  # noqa: E501
from gitea_api.rest import ApiException


class TestMiscellaneousApi(unittest.TestCase):
    """MiscellaneousApi unit test stubs"""

    def setUp(self):
        self.api = MiscellaneousApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_node_info(self):
        """Test case for get_node_info

        Returns the nodeinfo of the Gitea application  # noqa: E501
        """
        pass

    def test_get_signing_key(self):
        """Test case for get_signing_key

        Get default signing-key.gpg  # noqa: E501
        """
        pass

    def test_get_version(self):
        """Test case for get_version

        Returns the version of the Gitea application  # noqa: E501
        """
        pass

    def test_render_markdown(self):
        """Test case for render_markdown

        Render a markdown document as HTML  # noqa: E501
        """
        pass

    def test_render_markdown_raw(self):
        """Test case for render_markdown_raw

        Render raw markdown as HTML  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
