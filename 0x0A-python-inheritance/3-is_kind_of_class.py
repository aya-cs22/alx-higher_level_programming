#!/usr/bin/python3
""""Module with the method lookpu"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    for subclass in obj.__class__.__mro__[1:]:
        if subclass == a_class:
            return True
    return False
