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

        def area(self):
            """"calculate area of Square."""

            self.__size = size
            return self.__size * self.__size
