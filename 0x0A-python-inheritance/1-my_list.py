#!/usr/bin/python3
"""Class inherits from list"""


class MyList(list):
    """inherits from list
    Public instance method:
    prints the list, but sorted (ascending sort)
    """
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
