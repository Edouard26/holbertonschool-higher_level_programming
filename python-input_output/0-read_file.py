#!/usr/bin/python3
"""
    writes a string to a text file
"""


def read_file(filename=""):
    """
        function that read a file using with
    """

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
