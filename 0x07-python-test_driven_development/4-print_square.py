#!/usr/bin/python3
"""prints a square with the character #"""
def print_square(size):
    """checks size's type"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
