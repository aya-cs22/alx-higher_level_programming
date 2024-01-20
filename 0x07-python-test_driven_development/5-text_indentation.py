#!/usr/bin/python3
"""Module for  prints a square with the character #"""


def text_indentation(text):
    """text indent"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if char in [".", "?", ":"]:
            print()
            print()
        print(char, end="")
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")      
