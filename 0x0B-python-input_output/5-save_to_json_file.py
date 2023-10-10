#!/usr/bin/python3
"function to write to JSON"
import json


def save_to_json_file(my_obj, filename):
    "write an object to text file"
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
