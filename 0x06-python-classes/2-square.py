#!/usr/bin/python3
  2 """creating module square"""
  3 
  4 
  5 class Square:
  6     """creating square classs
  7     with conditional statements"""
  8     def __init__(self, size = 0):
  9     """initialization"""
 10         if size is not isdigit():
 11             raise TypeError("size must be an intger")
 12         elif size < 0:
 13             raise ValueError("size must be >=0")
 14         else:
 15             self.__size__ = size
