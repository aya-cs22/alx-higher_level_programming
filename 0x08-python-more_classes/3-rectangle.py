#!/usr/bin/python3

class Rectangle:
    """Define the Rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes the Rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get for the private instance attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set for the private instance attribute width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
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
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        str = ""
        if self.__height == 0 and self.__width == 0:
            for row in range(self.height):
                str += "#" * self.width + '\n'
        return str
