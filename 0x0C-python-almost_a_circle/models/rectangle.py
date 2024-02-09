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
        if not isinstance(width, int):
            raise TypeError("width of the attribute> must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        '''height method'''
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height of the attribute> must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
    @property
    def x(self):
        '''x method'''
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x of the attribute> must be an integer")
        if x < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = x
    @property
    def y(self):
        '''y method'''
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y of the attribute> must be an integer")
        if y < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = y

    def area(self):
        '''returns the area ofa rectangle'''
        return self.__width * self.__height
