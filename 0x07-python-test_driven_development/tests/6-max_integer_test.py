#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max integers"""
    def check_module_docstring(self):
        """Checks a module docstring"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def check_func_docstring(self):
        """Checks for docstring of the function"""
        n = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(n) > 1)

    def check_empty_list(self):
        """Checks if the list is empty"""
        list = []
        self.assertIsNone(max_integer(list))

    def check_no_arg(self):
        """Checks if there are no arguments passed"""
        self.assertIsNone(max_integer())

    def check_one_elem(self):
        """Checks when there is only one element in list"""
        list = [1]
        self.assertEqual(max_integer(list), 1)

    def check_positive_list(self):
        """Checking with all positive integers"""
        list = [0, 1, 2, 3, 4, 5]
        self.assertEqual(max_integer(list), 5)

    def check_max_middle(self):
        """Checks max if max was in the middle of list"""
        list = [0, 1, 100, 4, 5]
        self.assertEqual(max_integer(list), 100)

    def check_max_beginning(self):
        """Checks max if max at start"""
        list = [100, 0, 1, 2, 3]
        self.assertEqual(max_integer(list), 100)

    def check_max_end(self):
        """Checks if max at the end of list"""
        list = [0, 1, 2, 3 , 100]
        self.assertEqual(max_integer(list), 100)

    def check_one_negative_elem(self):
        """Checks for the max element with one element negative"""
        list = [-1, 0, 1, 2, 4]
        self.assertEqual(max_integer(list), 4)

    def check_negative_list(self):
        """Checks for max integer within all negative integers"""
        list = [-4, -3, -2, -1]
        self.assertEqual(max_integer(list), -1)

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_no_int_arg(self):
        """Checks for non-integer elements"""
        string = [1, 2, "string", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)

    if __name__ == "__main__":
        unittest.main()
