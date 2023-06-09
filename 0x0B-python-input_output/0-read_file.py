#!/usr/bin/python3
"""readfile Module"""


def read_file(filename=""):
    """a function that reads a text file
    (UTF8) and
    prints it to stdout
    """
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end='')
