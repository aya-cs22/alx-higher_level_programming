#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a square"""

    def __init__(self, size):
        """Constructor

        Args:
            size: length of a side of the square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than Zero.
        """
        self.__size = size
        if not isinstance(size ,int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
