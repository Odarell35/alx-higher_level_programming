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
		return self.width

	@size.setter
	def size(self, value):
		"""setter"""
		self.height = value
		self.width = value

	def __str__(self):
		"""string representation"""
		return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
         		self.y, self.width)

	def update(self, *args, **kwargs):
		"""args and kwargs"""
		if(args):
			if len(args) >= 1:
				self.id = args[0]
			if len(args) >= 2:
				self.size = args[1]
			if len(args) >= 3:
				self.x = args[2]
			if len(args) >= 4:
				self.y = args[3]
		else:
			for key, value in kwargs.items():
				setattr(self, key, value)

