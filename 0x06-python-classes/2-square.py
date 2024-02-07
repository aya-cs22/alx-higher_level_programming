#!/usr/bin/python3
""""Defines a class square"""


class Square:
    """
    class Square that defines a square by: (based on 1-square.py)
    attribute:
    size: size of square (1 side)
    """
    def __init__(self, size=0):
        """
        creat anew instance of square (1 side)
        Args:
        size: length of a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        
