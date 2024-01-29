#!/usr/bin/python3
""""Module with the method lookpu


def is_kind_of_class(obj, a_class):
   check if obj is subclass of a_class
    if type(obj) is a_class:
        return True
    return False
"""
def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an instance of a class
    that inherited from the specified class; otherwise False.

    Parameters:
    - obj: The object to check.
    - a_class: The specified class.

    Returns:
    - True if obj is an instance of a_class or its subclass, otherwise False.
    """
    # Check if obj is an instance of a_class
    if isinstance(obj, a_class):
        return True

    # Check if obj is an instance of any subclass of a_class
    for subclass in obj.__class__.__mro__[1:]:
        if subclass == a_class:
            return True

    return False
