#!/usr/bin/env python3
"""
Module for demonstrating duck typing with shapes.
Implements an abstract Shape class and concrete Circle and Rectangle classes.
"""

from abc import ABC, abstractmethod
PI = 3.141592653589793


class Shape(ABC):
    """Abstract base class for shapes."""
    
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """A circle shape with a given radius."""
    
    def __init__(self, radius):
        """
        Initialize a Circle with a radius.
        
        Args:
            radius: The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """Calculate and return the area of the circle."""
        return PI * self.radius ** 2
    
    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * PI * self.radius


class Rectangle(Shape):
    """A rectangle shape with given width and height."""
    
    def __init__(self, width, height):
        """
        Initialize a Rectangle with width and height.
        
        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape.
    
    This function uses duck typing - it doesn't check the type of the shape,
    but instead relies on the shape having area() and perimeter() methods.
    
    Args:
        shape: Any object that implements area() and perimeter() methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
