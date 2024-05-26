#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_cases(self):
        # Test cases with regular lists
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_empty_list(self):
        # Test case with an empty list
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        # Test case with a single-element list
        self.assertEqual(max_integer([42]), 42)

    def test_duplicate_max(self):
        # Test case with duplicate max elements
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_mixed_types(self):
        # Test case with mixed types (should raise TypeError)
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'a', 4])

if __name__ == '__main__':
    unittest.main()
