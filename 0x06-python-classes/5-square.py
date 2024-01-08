#!/usr/bin/python3
"""Square module"""


class squar:
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
