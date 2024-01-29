#!/usr/bin/python3
""""module with class BaseGeometry"""


class BaseGeometry:
    """"BaseGeometry class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Method for validating the value.'''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format((name)))
""""module with class Rectangle"""


class Rectangle(BaseGeometry):
    """"Rectangle class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
