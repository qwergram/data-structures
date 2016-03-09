# -*- coding: utf-8 -*-
"""Double linked list implementation for Nodes."""


class DllNode(object):
    """Node class utilizing Node parent class."""

    def __init__(self, value, pointer=None, previous=None):
        """Intialize DLL Node."""
        if pointer is None or isinstance(pointer, DllNode):
            self.pointer = pointer
        else:
            raise TypeError("Pointer must point to a node object")
        self.value = value
        self.previous = previous


class Dll(object):
    """Double linked list class utilizing parents."""

    def __init__(self, initial_values=[]):
        """Build a DLL of specified Nodes out of non-list values."""
        if not isinstance(initial_values, list):
            initial_values = [initial_values]
        previous = None
        for item in initial_values:
            self.tail = DllNode(item, self.tail, previous)
            previous = item
