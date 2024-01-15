from models.square import Square
import unittest
import os
import sys


class TestSquare(unittest.TestCase):

    def setUp(self):
        self.temp_file = 'tests/test_models/test_sq_display.txt'

    def tearDown(self):
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    # Positive testing
    def test_normal_args_wo_keys_and_id(self):
        """Tests for if normal arguments are passed w/o id and keys"""
        sq1 = Square(4, 1, 3)
        sq2 = Square(6, 1, 1)
        self.assertEqual(sq1.size, 4)
        self.assertEqual(sq1.x, 1)
        self.assertEqual(sq1.y, 3)
        self.assertEqual(sq2.size, 6)
        self.assertEqual(sq2.x, 1)
        self.assertEqual(sq2.y, 1)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_normal_args_w_keys_and_id(self):
        """Tests for if normal arguments are passed w/id and keys"""
        sq1 = Square(size=4, x=1, y=3, id=2)
        sq2 = Square(size=6, x=1, y=1, id=3)
        self.assertEqual(sq1.size, 4)
        self.assertEqual(sq1.x, 1)
        self.assertEqual(sq1.y, 3)
        self.assertEqual(sq2.size, 6)
        self.assertEqual(sq2.x, 1)
        self.assertEqual(sq2.y, 1)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_area_method(self):
        """Tests for the area method of the Square"""
        sq1 = Square(4, 1, 1, 2)
        sq1_area = sq1.area()
        self.assertEqual(sq1_area, 16)

    def test_display_method(self):
        """Tests for the display method of the Square"""
        filename = "tests/test_models/test_sq_display.txt"
        sq1 = Square(4, 3, 3, 4)
        sq1_str = "[Square] (4) 3/3 - 4"
        sq1_display = "\n\n\n   ####\n   ####\n   ####\n   ####\n"
        self.assertEqual(sq1_str, str(sq1))
        self.assertEqual(sq1.area(), 16)
        with open(filename, "w") as f:
            sys.stdout = f
            sq1.display()
            sys.stdout = sys.__stdout__
        with open(filename, "r") as f:
            c_output = f.read()
        self.assertEqual(c_output, sq1_display)

    def test_string_method(self):
        """Tests the string method of the Square"""
        sq1 = Square(4, 1, 1, 12)
        sq1_str = "[Square] (12) 1/1 - 4"
        self.assertEqual(sq1_str, str(sq1))

    def test_update_method_wo_keys(self):
        """Tests for the update method of the Square w/o keys"""
        sq1 = Square(1, 2, 3, 4)
        sq1.update(10, 10, 10, 10)
        sq1_str = "[Square] (10) 10/10 - 10"
        self.assertEqual(sq1_str, str(sq1))

    def test_update_method_wo_keys(self):
        """Tests for the update method of the Square w/o keys"""
        sq1 = Square(1, 2, 3, 4)
        sq1.update(id=10, size=10, x=10, y=10)
        sq1_str = "[Square] (10) 10/10 - 10"
        self.assertEqual(sq1_str, str(sq1))

    def test_to_dictionary_method(self):
        """Tests the to_dictionary method of the Square"""
        sq1 = Square(4, 2, 2, 10)
        sq1_dict = sq1.to_dictionary()
        sq1_results = {
            "id": sq1.id,
            "size": sq1.size,
            "x": sq1.x,
            "y": sq1.y
        }
        self.assertEqual(sq1_dict, sq1_results)

    # Negative testing
    # size
    def testing_size_less_zero(self):
        """Testing if the size of the Square is less than zero"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 1, 2, 3)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 1, 2, 3)

    def testing_size_string(self):
        """Testing if the size of the Square is a string"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("square", 1, 2, 3)

    def testing_size_float(self):
        """Testing if the size of the Square is a float"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1.01, 2, 3, 4)

    def testing_size_float_inf(self):
        """Testinf if the size of the Square is a float infinite"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'), 2, 3, 4)

    def testing_size_list(self):
        """Tests if the size of the Square is a list"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3], 2, 3, 4)

    def testing_size_tuple(self):
        """Tests if the size of the Square is a tuple"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2), 2, 3, 4)

    def testing_size_dict(self):
        """Tests if the size of the Square is a dictionary"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"size": 1}, 2, 3, 4)

    # x
    def testing_x_less_zero(self):
        """Testing if the x of the Square is less than zero"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -1, 2, 3)

    def testing_x_string(self):
        """Testing if the x of the Square is a string"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "square", 2, 3)

    def testing_x_float(self):
        """Testing if the x of the Square is a float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, 1.01, 3, 4)

    def testing_x_float_inf(self):
        """Testinf if the x of the Square is a float infinite"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, float('inf'), 3, 4)

    def testing_x_list(self):
        """Tests if the x of the Square is a list"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, [1, 2, 3], 3, 4)

    def testing_x_tuple(self):
        """Tests if the x of the Square is a tuple"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, (1, 2), 3, 4)

    def testing_x_dict(self):
        """Tests if the x of the Square is a dictionary"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {"size": 1}, 3, 4)

    # y
    def testing_y_less_zero(self):
        """Testing if the y of the Square is less than zero"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -1, 3)

    def testing_y_string(self):
        """Testing if the y of the Square is a string"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "square", 3)

    def testing_y_float(self):
        """Testing if the y of the Square is a float"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, 1.01, 4)

    def testing_y_float_inf(self):
        """Testinf if the y of the Square is a float infinite"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, float('inf'), 4)

    def testing_y_list(self):
        """Tests if the y of the Square is a list"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, [1, 2, 3], 4)

    def testing_y_tuple(self):
        """Tests if the y of the Square is a tuple"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, (1, 2), 4)

    def testing_y_dict(self):
        """Tests if the y of the Square is a dictionary"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, {"size": 1}, 4)


if __name__ == "__main__":
    unittest.main()
