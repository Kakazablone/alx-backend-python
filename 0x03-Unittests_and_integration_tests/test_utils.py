#!/usr/bin/env python3
"""Parametrized & Patching test suite
"""

import unittest
from unittest.mock import patch


def memoize(func):
    """
    Memoize the given function.

    Args:
        func: The function to memoize.

    Returns:
        A memoized version of the input function.
    """
    cache = {}

    def memoized_func(*args):
        """wraps the original function (func)
        to provide caching"""
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return memoized_func


class TestMemoize(unittest.TestCase):
    """
    Unit tests for the `memoize` decorator.
    """

    def test_memoize(self):
        """
        Test `memoize` to ensure it correctly caches results.
        """

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        obj = TestClass()

        with patch.object(obj, 'a_method', return_value=42) as mock_method:
            result1 = obj.a_property()
            result2 = obj.a_property()

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
