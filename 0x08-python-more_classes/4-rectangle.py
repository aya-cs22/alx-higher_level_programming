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
        return self.__width * self.__height

    def perimeter(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += '#'
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        return self._draw_rectangle()

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
