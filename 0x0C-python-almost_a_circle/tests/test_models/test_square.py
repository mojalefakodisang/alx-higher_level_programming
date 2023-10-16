#!/usr/bin/python3
"""Unit Testing for Square class"""
import unittest
from models.square import Square
from models.base import Base

class TestingSquareId(unittest.TestCase):
    """Testing for Square ID"""

    def testing_id_increment(self):
        """Tests if id attribute increments when id == None"""
        sq1 = Base()
        sq2 = Base()
        self.assertEqual(sq1.id, sq2.id - 1)

    def testing_three_id(self):
        """Tests increment of id in three Square objects if id == None"""
        sq1 = Base()
        sq2 = Base()
        sq3 = Base()
        self.assertEqual(sq1.id, sq2.id - 1)
        self.assertEqual(sq2.id, sq3.id - 1)
        self.assertEqual(sq1.id, sq3.id - 2)

    def testing_four_id(self):
        """Tests increment of id in four Square obj if id == None"""

        sq1 = Base()
        sq2 = Base()
        sq3 = Base()
        sq4 = Base()
        self.assertEqual(sq1.id, sq4.id - 3)
        self.assertEqual(sq1.id, sq3.id -2)

class TestingSquareArguments(unittest.TestCase):
    """Test for arguments of the Square in non-keyword mode"""

    def testing_no_arguments(self):
        """Tests for return if no arguments"""
        with self.assertRaises(TypeError):
            Square()

    def testing_one_argument(self):
        """Test for return if one argument passed"""
        sq1 = Square(1)
        self.assertEqual(sq1.size, 1)

    def testing_four_arguments(self):
        """Tests for return of four arguments"""
        sq1 = Square(1, 2, 3, 4)
        self.assertEqual(sq1.size, 1)
        self.assertEqual(sq1.id, 4)

class TestingSquareSize(unittest.TestCase):
    """Test for the value of Size in Square class"""

    def testing_normal_size(self):
        """Testing with regular values of size"""
        sq1 = Square(size=10)
        self.assertEqual(sq1.size, 10)

    def testing_negative_size(self):
        """Testing with negative values of size"""
        with self.assertRaises(ValueError):
            Square(size=-10)

    def testing_size_eq_zero(self):
        """Testing with zero value as size"""
        with self.assertRaises(ValueError):
            Square(size=0)

    def testing_size_none(self):
        """Testing if size is None"""
        with self.assertRaises(TypeError):
            Square(size=None)

    def testing_size_string(self):
        """Testing if size is a string"""
        with self.assertRaises(TypeError):
            Square(size="hello")

    def testing_size_float(self):
        """Testing if size is a float"""
        with self.assertRaises(TypeError):
            Square(size=1.01)

    def testing_size_float_inf(self):
        """Testing if size is a float infinity"""
        with self.assertRaises(TypeError):
            Square(size=float('inf'))

    def testing_size_list(self):
        """Testing if size is a list"""
        with self.assertRaises(TypeError):
            Square(size=[1, 2, 3, 4])

    def testing_size_dictionary(self):
        """Testing if size is a dictionary"""
        with self.assertRaises(TypeError):
            Square(size={'a': 1, 'b': 2})

    def testing_size_tuple(self):
        """Testing if size is a tuple"""
        with self.assertRaises(TypeError):
            Square(size=(0, 1))

class TestingSquareXandY(unittest.TestCase):
    """Tests for the value of X and Y in Sqaure"""

    def testing_x_y_regular(self):
        """Test for the value of x and y with regular values"""
        sq1 = Square(size=1, x=10, y=1)
        sq2 = Square(size=1, x=1, y=10)
        self.assertEqual(sq1.x, 10)
        self.assertEqual(sq2.y, 10)

    def testing_x_y_negative(self):
        """Test for the value of x and y with negative values"""
        with self.assertRaisesRegex(ValueError, "x must be > 0"):
            Square(size=1, x=-10, y=1)
        with self.assertRaisesRegex(ValueError, "y must be > 0"):
            Square(size=1, x=1, y=-10)

    def testing_x_y_string(self):
        """Test for the value of x and y if they are strings"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(size=1, x='hello', y=1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(size=1, x=1, y='hello')

    def testing_x_y_float(self):
        """Test for the value of x and y if they are floats"""
        with self.assertRaises(TypeError):
            Square(size=1, x=1.01, y=1)
            Square(size=1, x=1, y=1.01)
            Square(size=1, x=1.01, y=1.01)
            Square(size=1, x=float('inf'), y=1)
            Square(size=1, x=1, y=float('inf'))

    def testing_x_y_list(self):
        """Test for the value of x and y if they are lists"""
        with self.assertRaises(TypeError):
            Square(size=1, x=[1, 2, 3], y=1)
            Square(size=1, x=1, y=[1, 2, 4])
            Square(size=1, x=[1, 2], y=[1, 2])

    def testing_x_y_dictionary(self):
        """Test for the value of x and y if they are lists"""
        with self.assertRaises(TypeError):
            Square(size=1, x={'a': 1, 'b': 2}, y=1)
            Square(size=1, x= 1, y={'a': 1, 'b': 2})

    def testing_x_y_tuples(self):
        """Test for the value of x and y if they are tuples"""
        with self.assertRaises(TypeError):
            Square(size=1, x=(0, 1), y=1)
            Square(size=1, x=1, y=(0, 1))

class TestingSquareMethods(unittest.TestCase):
    """Testing for few methods inherited from both Base and Rectangle classes
        Methods:
           1. Testing for __str__ magic method
           2. Testing for update method
           3. Testing for area method
           4. Testing for to_dictionary method
           5. Testing for to_json_string method
           6. Testing for save_to_file method
    """

    def testing_for_str_args_method(self):
        """Test for normal return of __str__ with args on non-keyword mode"""
        sq1 = Square(1, 2, 3, 4)
        self.assertEqual(str(sq1), "[Square] (4) 2/3 - 1")

    def testing_for_str_key(self):
        """Test for normal return of __str__ with keyword args"""
        sq1= Square(size=1, x=2, y=3, id=4)
        self.assertEqual(str(sq1), "[Square] (4) 2/3 - 1")

    def testing_for_update(self):
        """Test for update of all the values of square object"""
        sq1 = Square(1, 2, 3, 4)
        sq1.update(size=10)
        self.assertEqual(sq1.size, 10)
        sq1.update(x=5)
        self.assertEqual(sq1.x, 5)
        self.assertEqual(str(sq1), "[Square] (4) 5/3 - 10")

    def testing_for_area_method(self):
        """Testing for area of the Square"""
        sq1 = Square(4, 1, 2, 3)
        self.assertEqual(sq1.area(), 16)

    def testing_for_to_dictionary(self):
        """Test for to_dictionary method"""
        sq1 = Square(1, 2, 3, 4)
        self.assertEqual(str(sq1), "[Square] (4) 2/3 - 1")
        sq1_dict = sq1.to_dictionary()
        self.assertEqual(sq1_dict, {'id': 4, 'size': 1, 'x': 2, 'y': 3})

if __name__ == '__main__':
    unittest.main()
