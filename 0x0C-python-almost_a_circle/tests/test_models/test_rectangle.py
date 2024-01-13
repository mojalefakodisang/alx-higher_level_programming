from models.rectangle import Rectangle
import unittest
import sys
import os


class TestRectangle(unittest.TestCase):
    """Tests Rectangle class"""

    def setUp(self):
        """Sets up the files with test results"""
        self.temp_file = 'tests/test_models/test_rec_display.txt'

    def tearDown(self):
        """Removes the test files"""
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    # Positive testing
    def test_normal_args(self):
        """Tests if normal arguments are passed"""
        r1 = Rectangle(3, 4, 2, 2)
        r2 = Rectangle(1, 2, 2, 4)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_normal_args_w_id(self):
        """Tests if normal arguments are passed with ID"""
        r1 = Rectangle(3, 4, 2, 2, 12)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 12)

    def test_area_method(self):
        """Tests for the area of the Rectangle with all normal values"""
        r1 = Rectangle(2, 2, 3, 4, 2)
        self.assertEqual(r1.area(), 4)

    def test_display_method(self):
        """Tests for the display method of the Rectangle"""
        filename = 'tests/test_models/test_rec_display.txt'
        r1 = Rectangle(2, 2, 2, 1, 2)
        r1_display = "\n  ##\n  ##\n"
        with open(filename, "w") as f:
            sys.stdout = f
            r1.display()
            sys.stdout = sys.__stdout__
        with open(filename, 'r') as f:
            c_output = f.read()
        self.assertEqual(c_output, r1_display)

    def test_str_method(self):
        """Tests for the string method of the Rectangle"""
        r1 = Rectangle(2, 2, 3, 3, 1)
        s_method = "[Rectangle] (1) 3/3 - 2/2"
        self.assertEqual(s_method, str(r1))

    def test_update_method_wo_keys(self):
        """Tests for the update method of the Rectangle, without keys"""
        r1 = Rectangle(1, 2, 3, 4, 10)
        r1.update(10, 10, 10, 10, 10)
        r1_string = "[Rectangle] (10) 10/10 - 10/10"
        self.assertEqual(r1_string, str(r1))

    def test_update_method_w_keys(self):
        """Tests for the update method of the Rectangle, without keys"""
        r1 = Rectangle(1, 2, 3, 4, 10)
        r1.update(id=10, width=10, height=9, x=10, y=10)
        r1_string = "[Rectangle] (10) 10/10 - 10/9"
        self.assertEqual(r1_string, str(r1))

    def test_to_dictionary_method(self):
        """Tests the to_dictionary method of the Rectangle"""
        r1 = Rectangle(id=1, width=2, height=4, x=1, y=1)
        r1_dict = r1.to_dictionary()
        r1_results = {
            "id": 1,
            "width": 2,
            "height": 4,
            "x": 1,
            "y": 1
        }
        self.assertEqual(r1_dict, r1_results)

    # Negative tests
    # width
    def test_width_less_zero(self):
        """Tests if width of the Rectangle is less than or equal zero"""
        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(-1, 3, 2, 2, 10)
        self.assertEqual(str(err.exception), "width must be > 0")

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(0, 3, 2, 2, 10)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_width_string(self):
        """Tests if width is a string"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("string", 3, 2, 2, 10)

    def test_width_float(self):
        """Tests if width is a float"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.01, 3, 2, 2, 10)

    def test_width_float_inf(self):
        """Tests if width is a float infinte"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 3, 2, 2, 10)

    def test_width_list(self):
        """Tests if width is a list"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 3, 2, 2, 10)

    def test_width_tuple(self):
        """Tests if width is a tuple"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2), 3, 2, 2, 10)

    def test_width_dict(self):
        """Tests if width is a dictionary"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"dict": 2}, 3, 2, 2, 10)

    # height
    def test_height_less_zero(self):
        """Tests if height of the Rectangle is less than or equal zero"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -1, 2, 2, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, 0, 2, 2, 10)

    def test_height_string(self):
        """Tests if height is a string"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "string", 2, 2, 10)

    def test_height_float(self):
        """Tests if height is a float"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, 1.01, 2, 2, 10)

    def test_height_float_inf(self):
        """Tests if height is a float infinte"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, float('inf'), 2, 2, 10)

    def test_height_list(self):
        """Tests if height is a list"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, [1, 2, 3], 2, 2, 10)

    def test_height_tuple(self):
        """Tests if height is a tuple"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, (1, 2), 2, 2, 10)

    def test_height_dict(self):
        """Tests if height is a dictionary"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, {"dict": 2}, 2, 2, 10)

    # x
    def test_x_less_zero(self):
        """Tests if x of the Rectangle is less than or equal zero"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 2, -1, 2, 10)

    def test_x_string(self):
        """Tests if x is a string"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, "string", 2, 10)

    def test_x_float(self):
        """Tests if x is a float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, 1.01, 2, 10)

    def test_x_float_inf(self):
        """Tests if x is a float infinte"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, float('inf'), 2, 10)

    def test_x_list(self):
        """Tests if x is a list"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, [1, 2, 3], 2, 10)

    def test_x_tuple(self):
        """Tests if x is a tuple"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, (1, 2), 2, 10)

    def test_x_dict(self):
        """Tests if x is a dictionary"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, {"dict": 2}, 2, 10)

    # y
    def test_y_less_zero(self):
        """Tests if y of the Rectangle is less than or equal zero"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 2, 2, -1, 10)

    def test_y_string(self):
        """Tests if y is a string"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 2, "string", 10)

    def test_y_float(self):
        """Tests if y is a float"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 2, 1.01, 10)

    def test_y_float_inf(self):
        """Tests if y is a float infinte"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 2, float('inf'), 10)

    def test_y_list(self):
        """Tests if y is a list"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 2, [1, 2, 3], 10)

    def test_y_tuple(self):
        """Tests if y is a tuple"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 2, (1, 2), 10)

    def test_y_dict(self):
        """Tests if y is a dictionary"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 2, {"dict": 2}, 10)


if __name__ == "__main__":

    try:
        unittest.main()
    except Exception as e:
        print(f"{e.__class__.__name__} - {e}")
