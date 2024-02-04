#!/usr/bin/python3
'''module for to_json_string method'''


import json


def from_json_string(my_str):
    """"that returns an object (Python data structure)"""
    return json.loads(my_str)
