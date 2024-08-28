#!/usr/bin/env python3

"""
Test suite for the `access_nested_map` function in the `utils` module.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for the `access_nested_map` function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: dict, path: tuple, expected: int) -> None:
        """
        Test `access_nested_map` with various inputs to ensure it returns the correct result.

        Args:
            nested_map (dict): The nested dictionary to search.
            path (tuple): The path to follow in the dictionary.
            expected (int): The expected result from the function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map: dict, path: tuple, expected_key: str) -> None:
        """
        Test `access_nested_map` to ensure it raises a KeyError with the expected key.

        Args:
            nested_map (dict): The nested dictionary to search.
            path (tuple): The path to follow in the dictionary.
            expected_key (str): The key that caused the KeyError.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Remove the surrounding quotes from the actual exception message
        actual_message = str(context.exception).strip("'")
        self.assertEqual(actual_message, expected_key)
