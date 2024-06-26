#!/usr/bin/python3
"""
function that write a string to a text file
"""


def write_file(filename="", text=""):
    """
        Writes a string to text file and returns number of characters written.
        Arguments:
            filename (str): File to write
            text (str): Text to add
    """
    count = 0
    with open(filename, 'w', encoding="utf-8") as f:
        count = f.write(text)
    return count
