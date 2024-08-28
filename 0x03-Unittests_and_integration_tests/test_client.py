#!/usr/bin/env python3
"""
Unit tests for the `GithubOrgClient` class from the `client` module.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for the `GithubOrgClient` class.
    """

    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"repos_url": "https://api.github.com/orgs/abc/repos"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, org_response, mock_get_json):
        """
        Test that the `org` method returns the correct value.

        Args:
            org_name: The name of the organization to test.
            org_response: Mocked response for the `org` method.
            mock_get_json: Mocked `get_json` method.
        """

        # Set up the mock to return the expected response
        mock_get_json.return_value = org_response

        # Create an instance of GithubOrgClient with the organization name
        client = GithubOrgClient(org_name)

        # Call the `org` method
        result = client.org

        # Check if `get_json` was called with the expected URL
        mock_get_json.\
            assert_called_once_with(client.ORG_URL.format(org=org_name))

        # Check if the returned value is correct
        self.assertEqual(result, org_response)


if __name__ == "__main__":
    unittest.main()
