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

        @property
        def width(self):
            '''width method'''
            return self.__width

        @width.setter
        def width(self, width):
            self.__width = width

        @property
        def height(self):
            '''height method'''
            return self.__height

        @height.setter
        def height(self, height):
            self.__height = height

        @property
        def x(self):
            '''x method'''
            return self.__x

        @x.setter
        def x(self, x):
            self.__x = x

        @property
        def y(self):
            '''y method'''
            return self.__y

        @y.setter
        def y(self, y):
            self.__y = y
