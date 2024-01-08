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
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
            def area(self):
                """Public instance method calculate Square Area."""

                return self.size * self.size
            def my_print(self):
                for i in range(self.size):
                    for j in range(self.size):
                        print("#", end='\n')
                    print()
