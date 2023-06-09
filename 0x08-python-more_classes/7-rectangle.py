#!/usr/bin/python3
"""Module: empty class """


class Rectangle:
    """ Class that defines rectangle
        Private attribute:
        width , height
        class attribute:
        number_of_instances
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialization of attributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ calculate the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ calculate perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints the rectangle in #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            sym = str(self.print_symbol)
            return ((sym*self.__width + "\n")*self.__height)[:-1]

    def __repr__(self):
        """prints string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Print message when instances deleted """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
