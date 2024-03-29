#!/usr/bin/python3
""""Module with the method lookpu"""


def inherits_from(obj, a_class):
    '''Determines if an object is a true subclass of a_class.'''
    for subclass in obj.__class__.__mro__[1:]:
        if subclass == a_class:
            return True
    return False
