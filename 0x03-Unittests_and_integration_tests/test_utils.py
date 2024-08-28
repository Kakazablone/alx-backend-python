#!/usr/bin/env python3

"""
Test suite for the `get_json` function in the `utils` module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json

class TestGetJson(unittest.TestCase):
    """
    Unit tests for the `get_json` function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')  # Patch `requests.get` in the `utils` module
    def test_get_json(self, test_url: str, test_payload: dict, mock_get: Mock) -> None:
        """
        Test `get_json` to ensure it returns the expected result and `requests.get` is called correctly.
        
        Args:
            test_url (str): The URL to pass to `get_json`.
            test_payload (dict): The payload that the mocked `requests.get` will return.
            mock_get (Mock): The mock object for `requests.get`.
        """
        # Configure the mock to return a response with the desired JSON payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function with the test URL
        result = get_json(test_url)

        # Check that `requests.get` was called exactly once with the correct URL
        mock_get.assert_called_once_with(test_url)
        
        # Check that the result from `get_json` matches the test payload
        self.assertEqual(result, test_payload)
