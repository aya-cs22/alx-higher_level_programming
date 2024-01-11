#!/usr/bin/python3
"""module for Rectangle class"""


class Rectangle:
    """define the Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get for the private instance attr width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set for the private instance attr width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """get for the private instance attr height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set for the private instance attr height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
