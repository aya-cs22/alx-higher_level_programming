#!/usr/bin/python3
""""Defines a class TestMaxInteger"""


import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    """"a class for max number in list"""
    def test_max_at_the_end(self):
        """"testing for at the end of list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_the_beginning(self):
        """"testing for at the beginning of list"""
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def test_max_at_the_middle(self):
        """"testing for at the middle of list"""
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_max_at_the_end(self):
        """"testing for at the end of list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_the_one_negative(self):
        """"testing for one negative number in the list"""
        self.assertEqual(max_integer([1, 2, -7, 4]), 4)

    def test_max_at_the_only_negative(self):
        """"testing for one negative number in the list"""
        self.assertEqual(max_integer([-1, -2, -7, -4]), -1)

    def test_max_at_the_empty(self):
        """"testing for one negative number in the list"""
        self.assertEqual(max_integer([]), None)

    def test_max_at_the_empty(self):
        """"testing for one negative number in the list"""
        self.assertEqual(max_integer([5]), 5)
    
if __name__=='main_':
    unittest.main()
