#!/usr/bin/python3
""" Module """


class Square:
    """ Square class create """
    def __init__(self, size=0):
        """
        initialize square"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
            set square square area"""
        return self.__size ** 2

    def my_print(self):
        """ print to stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
