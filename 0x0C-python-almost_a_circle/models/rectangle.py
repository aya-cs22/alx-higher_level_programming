#!/usr/bin/python3
"""class Rectangle"""

from models.base import Base


class Rectangle(Base):
    '''A subclass of Base class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Instatiation of a new subclass rectangle
        Args:
        width and height and x and y and id
        '''

        super().__init__(id)

    def width_getter(self):
        '''width method'''
        return self.__width

    def width_setter(self, width):
        self.__width = width

    def height_getter(self):
        '''height method'''
        return self.__height

    def height_setter(self, height):
        self.__height = height

    def x_getter(self):
        '''x method'''
        return self.__x

    def x_setter(self, x):
        self.__x = x

    def y_getter(self):
        '''y method'''
        return self.__y

    def y_setter(self, y):
        self.__y = y
