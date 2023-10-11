#!/usr/bin/python3
"function that checks if a class inherited"


def inherits_from(obj, a_class):
    "check if object is an inherited instance of class"
    if issubclass(type(obj), a_class) and type(obj)  != a_class:
        return True
    return False
