#!/usr/bin/python3
"define a function that adds attribute to an object"


def add_attribute(obj, key, value):
    "add new attributes to an object if possible"
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
