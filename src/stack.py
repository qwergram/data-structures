# -*- coding: utf-8 -*-
"""Stack subclass of Linked_list to add stack logic functionality."""
from linked_list import Node, LinkedList


class Stack(LinkedList):
    """Stack subclass of LinkedList."""

    def push(self, value):
        """Add a Node value to tail of Stack."""
        self.tail = Node(value, self.tail)

    def pop(self):
        """Override LinkedList pop to remove tail stack."""
        if not self.tail:
            raise IndexError("No items in list to pop")
        current = self.tail.value
        self.tail = self.tail.pointer
        return current
