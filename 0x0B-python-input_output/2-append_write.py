#!/usr/bin/python3
""""append a file method"""


def append_write(filename="", text=""):
    """"that append a text file"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
