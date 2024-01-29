#!/usr/bin/python3
""""Module with the method lookpu"""


def is_kind_of_class(obj, a_class):
    """"check if obj is subclass of a_class"""
    if type (obj) is a_class:
        return isinstance(obj, a_class)
    return False
