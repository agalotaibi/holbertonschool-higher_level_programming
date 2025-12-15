#!/usr/bin/python3
"""
This module contains the class MyList which inherits from list.
"""


class MyList(list):
    """
    A subclass of list that includes a method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        Note:
            This method prints a sorted copy of the list and does not
            modify the actual instance of the list.
        """
        # We use the built-in sorted() function because it returns a new list
        # and leaves the original list instance (self) unchanged.
        print(sorted(self))
