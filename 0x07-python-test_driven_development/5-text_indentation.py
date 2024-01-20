#!/usr/bin/python3
"""Module for  prints a square with the character #"""


def text_indentation(text):
    """text indent"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        print(char, end="")
        if char in ".?:":  # لو كان الحرف من العلامات المحددة
            print()  # تطبع مسافتين
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")      
