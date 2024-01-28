#!/usr/bin/python3
""""Module with the method lookpu"""


def is_same_class(obj, a_class):
    '''check if object an instance of specified class'''
    if type(obj) is a_class:
        return True
    return False
