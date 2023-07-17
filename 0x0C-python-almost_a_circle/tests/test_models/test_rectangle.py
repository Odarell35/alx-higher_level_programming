#!/usr/bin/python3
"""Test for the Rectangle class"""

import unittest
import json
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):
	"""testing rectangle class"""
	def test_width(self):
		"""how width functions"""
		self.assertEqual(self.r1.width, 10)
		self.assertEqual(self.r2.width, 2)
	
	def test_height(self):
		"""how height functions"""
		self.assertEqual(self.r1.height, 10)
		self.assertEqual(self.r2.height, 3)
	
	def test_x(self):
		"""how x functions"""
		self.assertEqual(self.r1.x, 0)
		self.assertEqual(self.r2.x, 4)

	def test_y(self):
		"""how y functions"""
		self.assertEqual(self.r1.y, 0)
		self.assertEqual(self.r2.y, 0)
	def test_area(self):
		"""test area"""
		with self.assertRaises(TypeError):
			r = self.r1.area(1)

	def test_str_(self):
		"""testing string representation"""
		self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 10/10")
		self.assertEqual(str(self.r2), "[Rectangle] (2) 4/0 - 2/3")

	def test_display(self):
		"""testing display()"""
		with self.assertRaises(TypeError):
			self.r1.display(1)
