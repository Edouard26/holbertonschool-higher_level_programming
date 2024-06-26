#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""

def add_integer(a, b=98):


    """
    Adds two integers.

    Args:
        a: The first integer or float.
        b: The second integer or float, default is 98.

    Returns:
        The sum of a and b, casted to integers.

    Raises:
        TypeError: If either a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
