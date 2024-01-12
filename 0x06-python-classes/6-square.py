#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Constructor

        Args:
            size (int): Length of a side of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    @property
    def position(self):
        return self.__size

    @position.setter
    def size(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(x, int) and x > 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value
    def area(self):
        """Public instance method to calculate Square Area."""
        return self.size * self.size
    def my_print(self):
        if self.size == 0:
            print("")
            return
        else:
