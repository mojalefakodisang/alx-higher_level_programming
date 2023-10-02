#!/usr/bin/python3
""" Module that has a class rectangle"""


class Rectangle:
    """ Class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Checks if the two rectangles are the same

            Args:
                rect_1: first rectangle
                rect_2: second rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __init__(self, width=0, height=0):
        """ Method that initializes attributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ Prints message if instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """ Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle

            Args:
                value: value to be set as width
        """
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle

            Args:
                value: value to be set as height
        """
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Gets area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ Gets perimeter of the rectangle"""
        perimeter = 0
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        """ Prints the rectangle"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))

        return string

    def __repr__(self):
        """ Representation of rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
