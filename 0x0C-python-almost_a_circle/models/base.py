#!/usr/bin/python3
"""Module: Base"""

import json


class Base:
	"""class base"""
	__nb_objects = 0

	def __init__(self, id=None):
		"""class constructor"""
		if id is not None:
			self.id = id
		else:
			Base.__nb_objects +=1
			self.id = Base.__nb_objects

	@staticmethod
	def to_json_string(list_dictionaries):
		"""returns the JSON string representation 
		of list_dictionaries"""
		if not list_dictionaries:
			return "[]"
		return json.dumps(list_dictionaries)
		
	@classmethod
	def save_to_file(cls, list_objs):
		""" dictionary to json"""
		empty_list = []
		with open (cls.__name__ + ".json", mode= "w", encoding="utf-8") as myfile:
			if list_objs:
				for objs in list_objs:
					empty_list.append(obj.to_dictionary())
			myfile.write(cls.to_json_string(empty_list))
	@staticmethod
	def from_json_string(json_string):
		"""returns the list of the JSON string representation"""
		if not json_string:
			return "[]"
		return json.loads(json_string)
	@classmethod
	def create(cls, **dictionary):
		"""returns an instance with all
		attributes already set"""
		if cls.__name__ == 'Rectangle':
			a = cls(1, 1)
		if cls.__name__ == 'Square':
			a = cls(1)
		a.update(**dictionary)
		return a 
