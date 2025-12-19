#!/usr/bin/env python3
"""
modeul Keeping Track of Iteration.
"""


class Fish:
    """Represents a fish that can swim in water."""

    def swim(self):
        """Fish swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Where the fish lives."""
        print("The fish lives in water")


class Bird:
    """Represents a bird that can fly in the sky."""

    def fly(self):
        """Bird flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Where the bird lives."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A flying fish that inherits from both Fish and Bird.
    
    Note: The order matters! Fish comes before Bird in the inheritance list,
    so Fish's methods take precedence in the MRO when we don't override them.
    """

    def fly(self):
        """Override Bird's fly method with flying fish specific behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override Fish's swim method with flying fish specific behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Override the habitat method from both parents.
        Since both Fish and Bird have habitat(), we need to override it
        to avoid ambiguity and provide the correct behavior.
        """
        print("The flying fish lives both in water and the sky!")
