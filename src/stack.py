# -*- coding: utf-8 -*-
"""Stack like functionality composed of Linked List object."""
from linked_list import Node, LinkedList


class Stack(object):
    """Define a stack object."""

    def __init__(self, value=[]):
        """Stack initialization composed of linkedlist."""
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
