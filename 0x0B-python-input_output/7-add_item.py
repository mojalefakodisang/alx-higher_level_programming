#!/usr/bin/python3
"""Module containing add_item method"""
import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_list.json"
if not os.path.isfile(filename):
    save_to_json_file([], filename)

my_list = load_from_json_file(filename)

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

save_to_json_file(my_list, filename)
