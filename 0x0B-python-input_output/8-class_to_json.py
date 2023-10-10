#!/usr/bin/python3
"function to define JSON file from python class"


def class_to_json(obj):
    "return __dict__ representaion"
    return obj.__dict__
