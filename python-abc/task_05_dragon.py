#!/usr/bin/env python3
"""
Module for demonstrating mixin classes.

This module contains mixin classes that provide swimming and flying
capabilities, which can be combined with other classes.
"""


class SwimMixin:
    """
    A mixin class that provides swimming capability.
    
    This mixin adds the ability to swim to any class that inherits from it.
    Mixins are meant to be combined with other classes and should focus on
    providing a single, specific piece of functionality.
    """

    def swim(self):
        """Make the creature swim."""
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class that provides flying capability.
    
    This mixin adds the ability to fly to any class that inherits from it.
    """

    def fly(self):
        """Make the creature fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that can both swim and fly.
    
    This class inherits from both SwimMixin and FlyMixin, demonstrating
    how mixins can be composed to give a class multiple capabilities.
    The Dragon class combines the swimming and flying abilities provided
    by the mixins with its own dragon-specific behavior.
    """

    def roar(self):
        """Make the dragon roar."""
        print("The dragon roars!")
