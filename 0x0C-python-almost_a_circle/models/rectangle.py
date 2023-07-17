#!/usr/bin/python3
"""Rectangle Module"""
from .base import Base


class Rectangle(Base):
	"""class that inherits from Base"""
	def __init__(self, width, height, x=0, y=0, id=None):
		""" class constructor """
		self._width = width
		self._height = height
		self._x = x
		self._y = y
		super().__init__(id)

	@property
	def width(self):
		"""getter for attribute"""
		return self._width
	
	@property
	def height(self):
		"""getter for attribute"""
		return self._height
	
	@property
	def x(self):
		"""getter for attribute"""
		return self._x
	
	@property
	def y(self):
		"""getter for attribute"""
		return self._y

	@width.setter
	def width(self, value):
		"""setter for width"""
		if type(value) is not int:
			raise TypeError(" width must be an integer")
		if value <= 0:
			raise ValueError("width must be > 0")
		self._width = value
	
	@height.setter
	def height(self, value):
		"""setter for height"""
		if type(value) is not int:
			raise TypeError("height must be an integer")
		if value <= 0:
			raise ValueError("height must be > 0")
		self._height = value

	@x.setter
	def x(self, value):
		"""setter for x"""
		if type(value) is not int:
			raise TypeError("x must be an integer")
		if value < 0:
			raise ValueError("x  must be >= 0")
		self._x = value

	@y.setter
	def y(self, value):
		"""setter for y"""
		if type(value) is not int:
			raise TypeError("y  must be an integer")
		if value <0:
			raise ValueError("y  must be >= 0")
		self._y = value

	def area(self):
		""" returns the area value of the Rectangle instance."""
		return self._width * self._height
