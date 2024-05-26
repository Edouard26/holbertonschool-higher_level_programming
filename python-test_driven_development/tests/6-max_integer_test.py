#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import os
import sys
import unittest

# Add parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    # Your test cases here...
