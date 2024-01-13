"""Model that contain Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): x spacing. Defaults to 0.
            y (int, optional): y spacing. Defaults to 0.
            id (_type_, optional): id of the object. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def _integer_validator(self, name, value, zeroable=False):
        """Validates any integers for a rectangle

        Args:
            name (str): name of the value
            value (_type_): value of the name
            zeroable (bool, optional): checks if it >= 0 or <= 0

        Raises:
            TypeError: {name} must be an integer
            ValueError: {name} must be > 0
            ValueError: {name} must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0 and zeroable is False:
            raise ValueError(f"{name} must be > 0")
        if value < 0 and zeroable is True:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        """Gets the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Stes the value of the Rectangle"""
        self._integer_validator("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Gets the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle"""
        self._integer_validator("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Gets the x of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x of the Rectangle"""
        self._integer_validator("x", value, True)
        self.__x = value

    @property
    def y(self):
        """Gets y of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets value for y of the Rectangle"""
        self._integer_validator("y", value, True)
        self.__y = value

    def area(self):
        """Area of the rectangle

        Returns:
            int: returns the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """Prints or displays the rectangle"""
        if self.width == 0 and self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for i in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def __str__(self):
        """String magic method"""
        return ("[{}] ({}) {}/{} - {}/{}".
                format("Rectangle", self.id, self.x,
                       self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Updates the attributes of the Rectangle"""
        if len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
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
        else:
            for k, v in kwargs.items():
                if k == "id":
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
        """Dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
