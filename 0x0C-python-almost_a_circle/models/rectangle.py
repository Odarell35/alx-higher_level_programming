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

	def width(self, value):
		"""setter for width"""
		self._width = value
	
	def height(self, value):
		"""setter for height"""
		self._height = value

	def x(self, value):
		"""setter for x"""
		self._x = value

	def y(self, value):
		"""setter for y"""
		self._y = value

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
