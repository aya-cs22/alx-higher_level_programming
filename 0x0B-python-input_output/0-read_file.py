#!/usr/bin/python3
""""method reads a file method"""


def read_file(filename=""):
    """"that reads a text file"""
    with open("UTF8", "r") as file:
        data = file.read()
    print(data)
