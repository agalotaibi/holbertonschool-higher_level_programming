#!/usr/bin/env python3
"""
modeul Keeping Track of Iteration.
"""


class CountedIterator:
    """An iterator wrapper that counts how many items have been iterated."""

    def __init__(self, iterable):
        """
        Initialize the CountedIterator.
        
        Args:
            iterable: Any iterable object (list, tuple, string, etc.)
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Return the iterator object itself.
        This makes CountedIterator compatible with for loops.
        """
        return self

    def __next__(self):
        """
        Get the next item and increment the counter.
        
        Returns:
            The next item from the iterator
            
        Raises:
            StopIteration: When there are no more items
        """

        item = next(self.iterator)
        
        self.count += 1
        
        return item

    def get_count(self):
        """
        Get the number of items that have been iterated.
        
        Returns:
            int: The current count of iterated items
        """
        return self.count
