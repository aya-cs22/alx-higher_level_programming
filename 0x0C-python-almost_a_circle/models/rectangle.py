#!/usr/bin/python3
"""class Rectangle"""

from models.base import Base


class Rectangle(Base):
    '''A subclass of Base class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Instantiation of a new subclass rectangle
        Args:
        width and height and x and y and id
        '''
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    def width(self):
        '''width getter'''

        return self.__width

    @width.setter
    def width(self, width):
        '''width setter
        args: width
        '''

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        '''height getter'''

        return self.__height

    @height.setter
    def height(self, height):
        '''height setter
        args: height
        '''

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        '''x getter'''

        return self.__x

    @x.setter
    def x(self, x):
        '''x setter
        args: x
        '''

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        '''y getter'''

        return self.__y

    @y.setter
    def y(self, y):
        '''y setter
        args: y
        '''

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """return the area value of the Rectangle"""
        return self.height * self.width

    def display(self):
        """class Rectangle by adding the public method """
        for g in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return a string representation of the Rectangle."""
        s = (
            f"[{Rectangle.__name__}] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}/{self.height}"
        )
        return s

    def update(self, *args, **kwargs):
        """Rectangle by adding the public method"""
        if args and len(args):
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
