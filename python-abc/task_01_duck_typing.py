#!/usr/bin/python3
"""
This modul is about Abstract Shap Class and its Subclasses
"""


from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    Class shape like blueprint for all the Subclasses.
    """
    @abstractmethod
    def area(self):
        """
        empty method return the area of a shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        empty method return the perimeter of a shape.
        """
        pass

class Circle(Shape):
    """
    class Circle inhert from the class shape.
    """
    def __init__(self, radius):
        """
        Initializes a new Circle instance.

        Args:
            radius (int): The radius of the circle.
        """
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.
        Formula: A = pi * radius ** 2.
        """
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """
        Calculates and returns the perimeter of the circle.
        Formula: p = 2 * pi * radius.
        """
        return 2 * math.pi * self.__radius

class Rectangle(Shape):
    """
    class Rectangle inhert from the class Shape.
    """
    def __init__(self, width, hieght):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__hieght = hieght

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        Formula: A = width * height.
        """
        return self.__width * self.__hieght

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        Formula: A = 2 * (width + height).
        """
        return 2 *  (self.__width + self.__hieght)


def shape_info(shape):
    """
    Standalone method print the perimeter and area.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
