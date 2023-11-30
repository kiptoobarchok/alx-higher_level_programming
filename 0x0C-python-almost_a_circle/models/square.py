#!/usr/bin/python3
"class that inherits from Rectangle"
from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
    
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value