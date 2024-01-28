#!/usr/bin/python3
""""Module with the method lookpu"""

class MyList(list):
    """"a class MyList that inherits from list"""

    def print_sorted(self):
        print (sorted(list(self)))
