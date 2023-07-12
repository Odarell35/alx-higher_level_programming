#!/usr/bin/python3
""" Class MyInt"""


class MyInt(int):
    """
    defined as a subclass of int
    """
    def __eq__(self, other):
        """
        overridden to invert the behavior of the == operator
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """ overridden to invert the behavior of the != operator"""
        return not super().__ne__(other)
