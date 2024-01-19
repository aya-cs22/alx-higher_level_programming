"""Module for add a+b method."""


def add_integer(a, b=98):
    """"Args:
    a: an integer number
    b: an integer number

    Raise:
    TypeError: if a, b are not int or float"""
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, int):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    else:
        return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
