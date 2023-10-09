#!/usr/bin/python3
"define a class"


def is_kind_of_class(obj, a_class):
    "check if object is instance or inherited instance of class"
    if isinstance(obj, a_class):
        return True
    return False
