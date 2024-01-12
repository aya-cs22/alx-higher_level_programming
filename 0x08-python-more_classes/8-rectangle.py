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
        """Get for the private instance attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set for the private instance attribute width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get for the private instance attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set for the private instance attribute height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        string = ""
        if self.width == 0 or self.height == 0:
            return ""
        for row in range(0, self.height):
            string += str(self.print_symbol) * self.width
            if row < self.height - 1:
                string += '\n'
        return string

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
