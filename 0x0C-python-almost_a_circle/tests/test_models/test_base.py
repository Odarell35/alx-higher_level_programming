#!/usr/bin/python3
""" Test cases for Base class"""

import unittest
import json
from models import base
Base = base.Base


class TestBase(unittest.TestCase):
	"""testing class base"""
	def test_many_args(self):
		"""when too many arguments are passed"""
		with self.assertRaises(TypeError):
			c = Base(1, 1)

	def test_no_id(self):
		""" whenid is none"""
		c = Base()
		self.assertEqual(c.id, 1)

	def test_id(self):
		""" when id is set to value"""
		c19 = Base(19)
		self.assertEqual(c19.id, 19)
	
	def test_nb_object(self):
		""" testing private class attribute"""
		c = Base(3)
		with self.assertRaises(AttributeError):
			print(c.nb_objects)
		with self.assertRaises(AttributeError):
			print(c.__nb_objects)
		
