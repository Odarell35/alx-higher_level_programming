#!/usr/bin/python3
"""Test for the Square class"""

import unittest
import json
from models import square
from models.base import Base
Square = square.Square


class TestSquare(unittest.TestCase):
	"""testing class asquare"""
	@classmethod
	def class_set(cls):
		"""set up for test"""
		Base._Base__nb_objects = 0
		cls.s1 = Square(1)
		cls.s2 = Square(2, 3)

	def test_id(self):
		""" normal functionality"""
		self.assertEqual(self.Square(1).id, 1)
		self.assertEqual(self.Square(2, 3).id, 2)

	def test_size(self):
		"""normal functionality"""
		self.assertEqual(self.s1.size, 1)
		self.assertEqual(self.s2.size, 2)

	def test_width(self):
		"""normal functionality"""
		self.assertEqual(self.s1.width, 1)
		self.assertEqual(self.s2.width, 2)

	def test_height(self):
		"""normal functionality"""
		self.assertEqual(self.s1.height, 1)
		self.assertEqual(self.s2.height, 2)

	def test_x(self):
		"""normal functionality"""
		self.assertEqual(self.s1.x, 0)
		self.assertEqual(self.s2.x, 3)

	def test_y(self):
		"""normal functionality"""
		self.assertEqual(self.s1.y, 0)
		self.assertEqual(self.s2.y, 0)
