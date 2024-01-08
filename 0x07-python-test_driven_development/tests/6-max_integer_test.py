#!/usr/bin/python3
"""Module containing unittest of Max integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class that tests for max integer in a list"""

    def test_empty_list(self):
        """Tests when the list is empty"""
        self.assertIsNone(max_integer([]))

    def test_normal_list(self):
        """Tests if a normal list is passed"""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)

    def test_normal_list_beginning(self):
        """Tests if a normal list is passed and max integer at the beginning"""
        self.assertEqual(max_integer([10, 1, 2, 3, 4]), 10)

    def test_normal_list_end(self):
        """Tests if a normal list is passed and max integer at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4, 10]), 10)

    def test_one_element_list(self):
        """Tests if a list has one element"""
        self.assertEqual(max_integer([10]), 10)

    def test_if_list(self):
        self.assertIsInstance(max_integer([10, 1, 2, 3, 4]), int)
