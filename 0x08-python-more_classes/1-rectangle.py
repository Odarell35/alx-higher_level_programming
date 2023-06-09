#!/usr/bin/python3
"""Module: empty class """


class Rectangle:
    """ Class that defines rectangle
        Private attribute:
        width , height
    """
    def __init__(self, width=0, height=0):
        """Initialization of attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """property to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter
        to set attribute to its value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ property getter
        to retrieve height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ property setter
        to set attribute to its value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
