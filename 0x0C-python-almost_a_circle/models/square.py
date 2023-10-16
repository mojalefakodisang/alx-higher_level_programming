#!/usr/bin/python3
"""The Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherited Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the Square class

            Args:
                size (int): size of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets new property of Square class"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates values of square based on arguments"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y, self.id)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y, self.id)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of Square"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """Magic method string"""
        str1 = "[Square] "
        str2 = f"({self.id}) "
        str3 = f"{self.x}/{self.y} "
        str4 = f"- {self.width}"
        return str1 + str2 + str3 + str4
