#!/usr/bin/python3
""""write a file method"""


def write_file(filename="", text=""):
    """"that write a text file"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
