#!/usr/bin/python3
""""Write on file Module"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file
    (UTF8)
    returns the number of characters written
    create the file if doesn’t exist
    overwrite the content of the file if it already exists
    """
    with open(filename, mode="w", encoding="utf-8") as myfile:
        return (myfile.write(text))
