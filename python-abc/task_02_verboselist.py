#!/usr/bin/env python3
"""
modeul that apply Extending the Python List 
with Notifications.
"""
class VerboseList(list):
    """A list that prints notifications when modified."""

    def append(self, item):
        """Add an item and notify."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Extend the list and notify."""
        count = len(items)
        super().extend(items)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove an item and notify."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item and notify."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
