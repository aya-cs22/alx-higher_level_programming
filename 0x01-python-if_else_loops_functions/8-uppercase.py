#!/usr/bin/python3
def uppercase(input_str):
    result = ""
    for word in input_str.split():
        result += word.capitalize() + ' '
        print(result.strip())
