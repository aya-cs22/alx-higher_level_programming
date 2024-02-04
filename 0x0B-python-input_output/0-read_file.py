#!/usr/bin/python3
""""method reads a file method"""


def read_file(filename=""):
    """"that reads a text file"""
    with open(str(filename), "r") as file:
        for line in file:
            print(line, end="")
