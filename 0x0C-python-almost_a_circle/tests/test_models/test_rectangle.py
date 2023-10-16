#!/usr/bin/python3
"""Unit Testing for Rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestingRectangleId(unittest.TestCase):
    """Testing for Rectangle Id"""

    def testing_id_increment(self):
        """Tests if id attribute increments when id  == None"""
        rec1 = Base()
        rec2 = Base()
        self.assertEqual(rec1.id, rec2.id - 1)

    def testing_three_id(self):
        """Tests increment of id in two rec when id == None"""
        rec1 = Base()
        rec2 = Base()
        rec3 = Base()
        self.assertEqual(rec1.id, rec2.id - 1)
        self.assertEqual(rec2.id, rec3.id - 1)
        self.assertEqual(rec1.id, rec3.id - 2)

    def testing_four_id(self):
        """Tests increment of id in four rec when id == None"""
        rec1 = Base()
        rec2 = Base()
        rec3 = Base()
        rec4 = Base()
        self.assertEqual(rec1.id, rec3.id - 2)
        self.assertEqual(rec1.id, rec4.id - 3)

class TestingRectangleArguments(unittest.TestCase):
    """Test for arguments of the Rectangle in non-keyword mode"""

    def testing_no_arguments(self):
        """Test for return if no arguments"""
        with self.assertRaises(TypeError):
            Rectangle()

    def testing_one_argument(self):
        """Test for return if one argument passed"""
        with self.assertRaises(TypeError):
            Rectangle()

    def testing_four_arguments(self):
        """Test for return of four arguments"""
        rec1 = Rectangle(1, 2, 3, 4)
        rec2 = Rectangle(5, 6, 7, 8)
        self.assertEqual(rec1.x, 3)
        self.assertEqual(rec1.id, rec2.id - 1)

    def testing_five_arguments(self):
        """Test for return of five arguments"""
        rec1 = Rectangle(1, 2, 3, 4, 5)
        rec2 = Rectangle(6, 7, 8, 9)
        self.assertEqual(rec1.id, 5)
        self.assertEqual(rec2.id, 1)

class TestingRectangleWidth(unittest.TestCase):
    """Testing Width of the Rectangle"""

    def testing_width_values(self):
        """Tests the values of width of rec"""
        rec1 = Rectangle(width=5, height=1, x=1, y=1)
        self.assertEqual(rec1.width, 5)

    def testing_width_eq_zero(self):
        """Tests the value of width if zero"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(width=0, height=1)

    def testing_width_negative(self):
        """Tests the value of width if negative"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(width=-1, height=1)

    def testing_width_as_None(self):
        """Tests the value of width if None"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(width=None, height=1)

    def testing_width_as_string(self):
        """Tests if the value of width is string"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(width="hello", height=1)

    def testing_width_as_float(self):
        """Tests if the value of width is a float"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(width=1.01, height=1)

    def testing_width_as_float_inf(self):
        """Tests for the value of width if float infinity"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(width=float('inf'), height=1)

    def testing_width_as_list(self):
        """Tests if the value of width is a list"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(width=[1, 2, 3], height=1)

    def testing_width_as_dictionary(self):
        """Tests if the value of width is a dictionary"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(width={'a': 1, 'b': 2}, height=1)

    def testing_width_as_tuple(self):
        """Tests if the value of width is a tuple"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(width=(1, 2, 3), height=1)

class TestingRectangleHeight(unittest.TestCase):
    """Tests for Rectangle Height"""

    def testing_height_normal(self):
        """Tests for the value of height with regular values"""
        rec1 = Rectangle(width=1, height=1, x=1, y=1)
        rec2 = Rectangle(width=1, height=10, x=1, y=1)
        self.assertEqual(rec1.height, 1)
        self.assertEqual(rec2.height, 10)

    def testing_height_negative(self):
        """Testing for the value of height if negative"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(width=1, height=-1)

    def testing_height_None(self):
        """Tests for the value of height if None"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(width=1, height=None)

    def testing_height_string(self):
        """Tests for the value of height if string"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(width=1, height="hello")

    def testing_height_float(self):
        """Tests for the value of height if float"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(width=1, height=1.01)

    def testing_height_float_inf(self):
        """Tests for the value of height if float infinity"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(width=1, height=float('inf'))

    def testing_height_list(self):
        """Testing for the value of height if list"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(width=1, height=[1, 2, 3])

    def testing_height_dictionary(self):
        """Testing for the value of height if dictionary"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(width=1, height={'a': 1, 'b': 2})

    def testing_height_tuple(self):
        """Tests for the value of height if tuple"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(width=1, height=(1, 2, 3))

class TestingRectangleX(unittest.TestCase):
    """Tests for the value of X in Rectangle"""

    def testing_x_regular(self):
        """Test for the value of x with regular values"""
        rec1 = Rectangle(width=1, height=1, x=1, y=1)
        rec2 = Rectangle(width=1, height=1, x=2, y=1)
        self.assertEqual(rec1.x, 1)
        self.assertEqual(rec2.x, 2)

    def testing_x_zero(self):
        """Test for the value of x if zero"""
        rec1 = Rectangle(width=1, height=1, x=0, y=1)
        self.assertEqual(rec1.x, 0)

    def testing_x_negative(self):
        """Tests fot the value of x if negative"""
        with self.assertRaisesRegex(ValueError, "x must be > 0"):
            Rectangle(width=1, height=1, x=-1, y=1)

    def testing_x_string(self):
        """Test for the value of x if string"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(width=1, height=1, x="hello", y=1)

    def testing_x_float(self):
        """Test for the value of x if float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(width=1, height=1, x=1.01, y=1)

    def testing_x_float_inf(self):
        """Test for the value of x if float infinity"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(width=1, height=1, x=float('inf'), y=1)

    def testing_x_list(self):
       """Tests for the value of x if list"""
       with self.assertRaisesRegex(TypeError, "x must be an integer"):
           Rectangle(width=1, height=1, x=[1, 2, 3], y=1)

    def testing_x_dictionary(self):
        """Tests for the value of x if dictionary"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(width=1, height=1, x={'a': 1, 'b': 2}, y=1)

class TestingRectangleY(unittest.TestCase):
    """Tests for the value of Y in Rectangle"""

    def testing_y_regular(self):
        """Test for the value of y if regular values"""
        rec1 = Rectangle(width=1, height=1, x=1, y=1)
        rec2 = Rectangle(width=1, height=1, x=1, y=2)
        self.assertEqual(rec1.y, 1)
        self.assertEqual(rec2.y, 2)

    def testing_y_zero(self):
        """Test for the value of y if zero"""
        rec1 = Rectangle(width=1, height=1, x=1, y=0)
        self.assertEqual(rec1.y, 0)

    def testing_y_negative(self):
        """Test for the value of y if negative"""
        with self.assertRaisesRegex(ValueError, "y must be > 0"):
            Rectangle(width=1, height=1, x=1, y=-1)

    def testing_y_string(self):
        """Test for the value of y if string"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(width=1, height=1, x=1, y="hello")

    def testing_y_float(self):
        """Test for the value of y if float"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(width=1, height=1, x=1, y=1.01)

    def testing_y_float_inf(self):
        """Test for the value of y if float infinity"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(width=1, height=1, x=1, y=float('inf'))

    def testing_y_list(self):
        """Test for the value of y if list"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(width=1, height=1, x=1, y=[1, 2, 3, 4])

    def testing_y_dictionary(self):
        """Test for the value of y if dictionary"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(width=1, height=1, x=1, y={'a': 1, 'b': 2})

class TestingRectangleMethods(unittest.TestCase):
    """Testing for string magic method of Rectangle

        Methods:
            1. Testing for __str__ magic method
            2. Testing for update method
            3. Testing for area of Rectangle
            4. Testing for to_dictionary method
            5. Testing for to_json_string method
            6. Testing for save_to_file method
            7. Testing for from_json_string method
            8. Testing for create method
            9. Testing for load_from_file method
    """

    def testing_normal_string(self):
        """test for normal return of Rectangle class"""
        rec1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(rec1), "[Rectangle] (5) - 3/4 - 1/2")

    def testing_normal_string_args(self):
        """Test for normal return of Rectangle class if args has keywords"""
        rec1 = Rectangle(width=1, height=2, x=3, y=4, id=5)
        self.assertEqual(str(rec1), "[Rectangle] (5) - 3/4 - 1/2")

    def testing_update_method_width(self):
        """Testing for update method for width"""
        rec1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(str(rec1), "[Rectangle] (1) - 10/10 - 10/10")
        rec1.update(width=5)
        self.assertEqual(str(rec1), "[Rectangle] (1) - 10/10 - 5/10")

    def testing_update_method_height(self):
        """Testing for update method for height"""
        rec1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(str(rec1), "[Rectangle] (1) - 10/10 - 10/10")
        rec1.update(height=5)
        self.assertEqual(str(rec1), "[Rectangle] (1) - 10/10 - 10/5")

    def testing_update_x_y(self):
        """Testing for update method for x and y attributes"""
        rec1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(str(rec1), "[Rectangle] (1) - 10/10 - 10/10")
        rec1.update(x=1, y=1)
        self.assertEqual(str(rec1), "[Rectangle] (1) - 1/1 - 10/10")

    def testing_area_rectangle(self):
        """Testing for area of the Rectangle"""
        rec1 = Rectangle(1, 5, 1, 1, 1)
        self.assertEqual(str(rec1), "[Rectangle] (1) - 1/1 - 1/5")
        self.assertEqual(rec1.area(), 5)

    def testing_to_dictionary(self):
        """Testing for to_dictionary method of Rectangle"""
        rec1 = Rectangle(5, 10, 2, 2, 1)
        self.assertEqual(str(rec1), "[Rectangle] (1) - 2/2 - 5/10")
        self.assertEqual(rec1.to_dictionary(),
                {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 2})

    def testing_to_json_string(self):
        """Testing for to_json_string method of Rectangle"""
        rec1 = Rectangle(10, 7, 2, 8, 1)
        self.assertEqual(str(rec1), "[Rectangle] (1) - 2/8 - 10/7")
        dictionary = rec1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary,
                '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')

if __name__ == '__main__':
    unittest.main()
