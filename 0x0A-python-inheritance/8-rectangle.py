#!/usr/bin/python3
"define a class"
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    "class inheriting from BaseGeometry"
    def __init__(self, width, height):
        "initialize a new rectangle"
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
