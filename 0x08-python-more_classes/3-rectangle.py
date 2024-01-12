#!/usr/bin/python3
class Rectangle:
    """Define the Rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes the Rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if isinstance(value, int) and value >= 0:
            self.__width = value
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        if isinstance(value, int) and value >= 0:
            self.__height = value
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
    def __str__(self):
        str = ""
        if self.width == 0 or self.height == 0:
            return ""
        for row in range(self.height):
            str += "#" * self.__width
            if row < self.height - 1:
                str += '\n'
        return str
