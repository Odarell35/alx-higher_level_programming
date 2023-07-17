#!/usr/bin/python3
"""Square module"""
from .rectangle import Rectangle


class Square(Rectangle):
	""""class square"""
	def __init__(self, size, x=0, y=0, id=None):
		""" instation"""
		super().__init__(size, size, x, y, id)
		self.size = size

	@property
	def size(self):
		"""getter"""
		return self.size

	@size.setter
	def size(self, value):
		"""setter"""
		self.height = value
		self.width = value

	def __str__(self):
		"""string representation"""
		return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
         		self.y, self.width)
