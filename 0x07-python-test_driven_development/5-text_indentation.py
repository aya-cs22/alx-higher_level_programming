#!/usr/bin/python3
"""Module for  prints a square with the character #"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if char in [".", "?", ":"]:
            print()
            print()
        print(char, end="")
        
