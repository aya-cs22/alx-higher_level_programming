#!/usr/bin/python3
'''module Object to a text file'''


import json


def save_to_json_file(my_obj, filename):
    """"that writes an Object to a text file, using a JSON"""
    with open(filename, 'a', encoding='utf-8') as file:
        return json.dump(my_obj, file)
