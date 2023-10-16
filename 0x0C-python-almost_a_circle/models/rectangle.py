#!/usr/python3
"""The rectangle module"""
from models.base import Base


class Rectangle(Base):
    """The Rectangle class inherited Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle class

            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
                x (int)
                y (int)
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Sets width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Gets width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Sets height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Gets height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Sets x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Gets x of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Sets y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Gets y of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Prints Rectangle with character #"""
        if self.width == 0 or self.height == 0:
            print("")

        for y in range(self.y):
            print("")

        for i in range(self.height):
            if self.x > 0:
                print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of Rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """Magic method that returns a string"""
        str1 = "[Rectangle] "
        str2 = f"({self.id}) "
        str3 = f"- {self.x}/{self.y} "
        str4 = f"- {self.width}/{self.height}"
        return str1 + str2 + str3 + str4
