# -*- coding: utf-8 -*-
"""Stack subclass of Linked_list to add stack logic functionality."""
from linked_list import Node, LinkedList


class Stack(object):
    """Stack subclass of LinkedList."""

    def __init__(self, value=[]):
        """Stack initailization composed of linkedlist."""
        self.ll = LinkedList(value)

    def push(self, value):
        """Add a Node value to tail of Stack."""
        self.ll.tail = Node(value, self.ll.tail)

    def pop(self):
        """Override LinkedList pop to remove tail stack."""
        if not self.ll.tail:
            raise IndexError("No items in list to pop")
        current = self.ll.tail.value
        self.ll.tail = self.ll.tail.pointer
        return current
