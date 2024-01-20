#!/usr/bin/python3
"""Module for  prints a square with the character #"""


def text_indentation(text):
    """text indent"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delim in (".?:"):
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
    print("{}".format(text), end="")
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")      
