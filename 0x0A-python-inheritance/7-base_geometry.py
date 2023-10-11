#!/usr/bin/python3
"define a class"


class BaseGeometry:
    "class"
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        "checks if parameter is an integer"
        if (type(value) != int):
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise TypeError(f"{self.name} must be greater than 0")
