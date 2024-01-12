#!/usr/bin/python3
"""empty class called rectangle"""


class Rectangle:
    """class that does nothing"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            str += '#' * self.width
            if row < self.height - 1:
                str += '\n'
        return str

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
