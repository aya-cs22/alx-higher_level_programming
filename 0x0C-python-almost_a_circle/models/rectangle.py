#!/usr/bin/python3
'''A module to write the class Rectangle that inherits from Base'''


from models.base import Base


class Rectangle(Base):
    '''A subclass of Base Class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Instatiation of a new subclass rectangle
        Args:
        width and height and x and y and id
        '''

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
