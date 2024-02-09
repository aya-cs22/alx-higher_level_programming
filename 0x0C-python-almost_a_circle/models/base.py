#!/usr/bin/python3
"""Class Base"""


class Base:
    '''A class to set self id'''

    __nb_objects = 0
    def __init__(self, id=None):
        '''instatiation
        Args: the id: None is default value'''

        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        
