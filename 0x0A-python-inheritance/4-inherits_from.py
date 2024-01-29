#!/usr/bin/python3
"""
check  if the object is
an instance of a class that inherited
(directly or indirectly) from the specified class

return true if it is, false otherwise
"""


def is_subclass_of(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class; otherwise False.

    Parameters:
    - obj: The object to check.
    - a_class: The specified class.

    Returns:
    - True if obj is an instance of a subclass of a_class, otherwise False.
    """
    return any(a_class in class_.__mro__ for class_ in obj.__class__.__mro__[1:])
