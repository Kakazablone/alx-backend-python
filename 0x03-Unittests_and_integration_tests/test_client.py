#!/usr/bin/env python3
"""
Unit tests for the `GithubOrgClient` class from the `client` module.
"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for the `GithubOrgClient` class.
    """

    @patch('client.GithubOrgClient.org',
           new_callable=unittest.mock.PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that `_public_repos_url` returns the
        correct URL based on the mocked `org` method.

        Args:
            mock_org: Mocked `org` property.
        """

        # Set up the mock to return a dictionary with the 'repos_url' key
        mock_org.return_value = \
            {"repos_url": "https://api.github.com/orgs/test_org/repos"}

        # Create an instance of GithubOrgClient with a test organization name
        client = GithubOrgClient("test_org")

        # Access the `_public_repos_url` property
        result = client._public_repos_url

        # Verify the result matches the expected URL
        self.assertEqual(result, "https://api.github.com/orgs/test_org/repos")


if __name__ == "__main__":
    unittest.main()
