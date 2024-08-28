#!/usr/bin/env python3

"""
Test suite for the `memoize` decorator in the `utils` module.
"""

import unittest
from unittest.mock import patch
from utils import memoize

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
