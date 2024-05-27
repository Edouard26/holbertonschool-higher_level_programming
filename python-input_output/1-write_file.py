#!/usr/bin/python3
"""
function that write a string to a text file
"""


def write_file(filename="", text=""):
    """
        Write a text file (UTF8) and return the number of characters written
        Arguments:
            filename (str): Text to add
    """
    count = 0
    with open(filename, encoding="utf-8") as f:
        count = f.write(text)
    return count

