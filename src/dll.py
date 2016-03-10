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

    tail = None

    def __init__(self, initial_values=[]):
        """Build a DLL of specified Nodes out of non-list values."""
        if not isinstance(initial_values, list):
            initial_values = [initial_values]
        for item in initial_values:
            initial = DllNode(item, pointer=self.tail, previous=None)
            current = DllNode(item, pointer=initial, previous=None)
            initial.previous = current
            self.tail = current

    def display(self):
        """Print and return formatted string displaying Node Chain."""
        cursor = self.tail
        cool_string = u""
        while cursor:
            cool_string += u"'{}', ".format(cursor.value)
            cursor = cursor.pointer
        if cool_string:
            cool_string = u'(' + cool_string[:-2] + u')'
            print(cool_string)
        return cool_string


    def insert(self, val):
        """Insert value into DL Node list."""
        if self.tail:
            cursor = self.tail
            while cursor.pointer:
                previous = cursor
                cursor = cursor.pointer
            cursor.pointer = DllNode(val, pointer=None, previous=previous)
        else:
            self.tail = DllNode(val)

    def append(self, val):
        """."""
        pass

    def pop(self):
        """."""
        pass

    def shift(self):
        """."""
        pass

    def remove(self, node):
        """."""
        pass
