#!/usr/bin/python3
'''
    class Square:
        that inherits from Rectangle
'''


from .rectangle import Rectangle

class Square(Rectangle):
    '''
        defining class Square
        attributes
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size

    def __str__(self):
        '''
        function to customize a tring representation
        '''
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
    
    @property
    def size(self):
        '''
        function to get size of square
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        function to set size of square and validate it
        '''
        self.width = value
        self.height = value