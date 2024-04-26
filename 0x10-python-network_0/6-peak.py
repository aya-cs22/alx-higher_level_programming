#!/usr/bin/python3
"""A module finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    max = list_of_integers[0]
    for i in range(len(list_of_integers)):
        current_num = list_of_integers[i]
        if current_num > max:
            max = current_num
    return max
