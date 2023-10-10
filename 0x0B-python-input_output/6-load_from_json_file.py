#!/usr/bin/python3
"function to read JSON file"
import json


def load_from_json_file(filename):
    "create python object from json file"
    with open(filename) as f:
        return json.load(f)
