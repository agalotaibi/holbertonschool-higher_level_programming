#!/usr/bin/python3
"""
This module defines a class named Rectangle based on 1-rectangle.py,
adding methods for calculating area and perimeter.
"""


class Rectangle:
    """
    Defines a rectangle with private width and height attributes,
    property setters/getters with validation, instance count
    and allows customizable print symbol.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (defaults to 0).
            height (int): The height of the rectangle (defaults to 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        Formula: A = width * height.
        """
        # Area = width * height
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        Returns 0 if width or height is 0.
        Formula: P = 2 * (width + height)
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns the string representation of the rectangle using #.
        If width or height is 0, returns an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""

        rect_lines = []
        for i in range(self.height):
            rect_lines.append(str(self.print_symbol) * self.width)

        return "\n".join(rect_lines)

    def __repr__(self):
        """
        Returns a string representation of the rectangle that can be used
        with eval() to recreate a new instance.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when the Rectangle instance is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the one with the bigger area.
        If both have the same area, returns rect_1.

        Args:
            rect_1: First rectangle to compare
            rect_2: Second rectangle to compare

        Returns:
            The rectangle with the larger area, or rect_1 if equal

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
