"""Empty class BaseGeometry"""
BaseGeometry = __import__('6-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
