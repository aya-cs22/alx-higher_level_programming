#!/usr/bin/python3
""""method reads a file method"""


def read_file(filename=""):
    """"that reads a text file"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
        print(data)
