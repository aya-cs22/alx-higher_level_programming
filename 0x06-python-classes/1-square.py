#!/usr/bin/python3
""""Defines aclass square"""


class Square:
    """"
    class that defines a square by: (based on 0-square.py)
    Attributes:
    size: size of a square (1 side).
    """
    def __init__(self, size):
        """"
        creat a new instance of square (1 side)
        Args:
        size: length of a side of the square.
        """
        self.__size = size
