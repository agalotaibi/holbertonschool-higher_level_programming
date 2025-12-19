#!/usr/bin/python3
"""
This modul is about Abstract Animal Class and its Subclasses
"""


from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Class Animal like blueprint for all the Subclasses.
    """
    @abstractmethod
    def sound(self):
        """
        empty method about the sound of the animal.
        """
        pass


class Dog(Animal):
    """
    class dog inhert from the class animal.
    """
    def sound(self):
        """
        method that return the sound of a dog.
        
        Return:
            dog sound bark
        """
        return "Bark"

class Cat(Animal):
    """
    class cat inhert from the class animal.
    """
    def sound(self):
        """
        method that return the sound of a cat.
        
        Return:
            cat sound meow
        """
        return "Meow"
