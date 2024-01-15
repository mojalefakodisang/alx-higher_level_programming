from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import os


class TestBase(unittest.TestCase):
    """Testing Base class instances - ID"""

    def test_id_None(self):
        """Test if class is initialize normally"""
        r1 = Base()
        r2 = Base()
        r3 = Base()
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, r3.id - 1)
        self.assertEqual(r3.id, r2.id + 1)
        self.assertGreater(r3.id, r1.id)

    def test_id_given(self):
        """Tests for ID if it is given"""
        r1 = Base()
        r2 = Base(14)
        r3 = Base()
        self.assertEqual(r1.id, r3.id - 1)
        self.assertEqual(r2.id, 14)
        self.assertEqual(r3.id, r1.id + 1)
        self.assertGreater(r2.id, r3.id)

    def test_id_str(self):
        """Tests for ID if a string"""
        r1 = Base("string")
        self.assertEqual(r1.id, 'string')

    def test_id_float(self):
        """Tests for ID if a float"""
        r1 = Base(1.01)
        self.assertEqual(r1.id, 1.01)

    def test_id_float_inf(self):
        """Tests for ID if a float infinite"""
        r1 = Base(float('inf'))
        self.assertEqual(r1.id, float('inf'))

    def test_id_list(self):
        """Tests for ID if a list"""
        r1 = Base([1, 2, 3])
        self.assertEqual(r1.id, [1, 2, 3])

    def test_id_tuple(self):
        """Tests for ID if a tuple"""
        r1 = Base((1, 2))
        self.assertEqual(r1.id, (1, 2))

    def test_id_dict(self):
        """Tests for ID if a dictionary"""
        r1 = Base({"string": 1})
        self.assertEqual(r1.id, {'string': 1})


class TestsBaseMethods(unittest.TestCase):
    """Tests for Base class static and class methods"""

    def setUp(self):
        self.temp_file = ['Base.json', 'Rectangle.json', 'Square.json'
                          'Base.csv', 'Rectangle.csv', 'Square.csv']

    def tearDown(self):
        for x in self.temp_file:
            if os.path.exists(x):
                os.remove(x)

    def testing_to_json_string_method(self):
        """Tests for converting list of dictionaries into JSON string"""
        r1 = Rectangle(10, 7, 2, 8)
        r1_dict = r1.to_dictionary()
        self.assertEqual(type(r1_dict), dict)
        json_dict = Base.to_json_string([r1_dict])
        self.assertEqual(type(json_dict), str)

    def testing_save_to_file_method(self):
        """Tests if the JSON string is written into a file"""
        sq1 = Square(2, 3, 4, 5)
        sq2 = Square(4, 2, 1, 4)
        Square.save_to_file([sq1, sq2])

        s_results_1 = '[{"id": 5, "size": 2, "x": 3, "y": 4}, '
        s_results_2 = '{"id": 4, "size": 4, "x": 2, "y": 1}]'
        s_results = s_results_1 + s_results_2
        with open('Square.json', "r") as f:
            c_output = f.read()
        self.assertEqual(s_results, c_output)

    def testing_from_json_string_method(self):
        """Tests if the JSON representation can be converted back
        to any Python data type
        """
        sq1 = Square(2, 3, 4, 5)
        sq2 = Square(4, 2, 1, 4)

        list_dict = [sq1.to_dictionary(), sq2.to_dictionary()]
        json_input = Square.to_json_string(list_dict)
        json_output = Square.from_json_string(json_input)

        self.assertEqual(type(json_input), str)
        self.assertEqual(type(json_output), list)

    def testing_create_method(self):
        """Tests if all attributes can be created"""
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)

        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.id, r2.id)

    def testing_load_from_file_method(self):
        """Tests for load from file method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        list_rectangle_input = [r1, r2]

        Rectangle.save_to_file(list_rectangle_input)
        l_output = Rectangle.load_from_file()
        r1_string = "[Rectangle] (1) 2/8 - 10/7"
        r2_string = "[Rectangle] (2) 0/0 - 2/4"
        self.assertEqual(str(l_output[0]), r1_string)
        self.assertEqual(str(l_output[1]), r2_string)

    def testing_save_to_file_csv_method(self):
        """Tests for the save to file into csv method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        list_rectangle_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangle_input)
        l_output = Rectangle.load_from_file_csv()
        r1_string = "[Rectangle] (1) 2/8 - 10/7"
        r2_string = "[Rectangle] (2) 0/0 - 2/4"
        self.assertEqual(str(l_output[0]), r1_string)
        self.assertEqual(str(l_output[1]), r2_string)


if __name__ == "__main__":
    unittest.main()
