#!/usr/bin/python3
"""script to adds all arguments to a Python list"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

open("add_item.json", "a")
try:
    y = load_from_json_file("add_item.json")
except ValueError:
    y = []

save_to_json_file(y + sys.argv[1:], "add_item.json")
