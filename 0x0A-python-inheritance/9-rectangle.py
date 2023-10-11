#!/usr/bin/python3
"define a class"
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    "class Rectangle inheriting from BaseGeometry"
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        s_tring = "[" + str(self.__class__.__name__) + "]"
        s_tring += str(self.__width) + "/" + str(self.__height)
        return s_tring
