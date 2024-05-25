#!/usr/bin/python3
""" Defines a Rectangle class """


class Rectangle:
    """
    class rectangle with width and height
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle


        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """
        Set width of rectangle

        Args:
            value (int): The width value to set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        """
        Set height of rectangle

        Args:
            value (int): The height value to set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Get the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
    def __str__(self):
        """Return string  representation of the rectangle """
        if self.width == 0 or self.height == 0:
            return ""
        rect_str = ""
        for _ in range(self.height):
            rect_str += '#' * self.width + '\n'
        return rect_str[:-1]
    def __repr__(self):
        """Return a string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.width, self.height)
    def __del__(self):
        """ Print a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")


