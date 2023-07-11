#!/usr/bin/python3
""" Create a class"""


class Student:
    """ a class Student that defines a student by:
    Public instance attributes:
    first_name
    last_name
    age
    Public method:retrieves a dictionary
    representation of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Public method:retrieves a dictionary
        representation of a Student instance
         """
        return (self.__dict__)
