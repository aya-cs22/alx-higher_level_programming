#!/usr/bin/python3
"""Module for  prints a square with the character #"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if char in [".", "?", ":"]:
            print()  # Print two newlines
        print(char, end="")  # Print newline if the text didn't end with a newline
        
