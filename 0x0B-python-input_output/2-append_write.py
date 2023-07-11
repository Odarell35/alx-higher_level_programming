#!/usr/bin/python3
"""Append to file"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file
    encoding:(UTF8)
    returns the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as myfile:
        return(myfile.write(text))
