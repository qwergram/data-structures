# -*- coding=utf-8 -*-
"""Hold sample code for number of classic data structures implemented in Python."""


class Node(object):
    """A class inheriting object that holds a value and pointer."""

    def __init__(self, value, pointer=None):
        """Build a Node object with specified value and pointer."""
        if pointer is None or isinstance(pointer, Node):
            self.pointer = pointer
        else:
            raise TypeError("Pointer must point to a node object")
        self.value = value


class LinkedList(object):
    """A class wrapper with Node linking methods."""
    tail = None

    def __init__(self, initial_values=[]):
        """Build a LinkedList of specified Nodes out of non-list values."""
        if not isinstance(initial_values, list):
            initial_values = [initial_values]
        for item in initial_values:
            self.tail = Node(item, self.tail)

    def insert(self, val):
        """Insert value into Linked Node list."""
        if self.tail:
            cursor = self.tail
            while cursor.pointer:
                cursor = cursor.pointer
            cursor.pointer = Node(val, None)
        else:
            self.tail = Node(val, None)

    def pop(self):
        """Return and remove head from Linked Node list."""
        cursor = self.tail
        previous = None
        if self.tail:
            if self.tail.pointer is None:
                previous = self.tail.value
                self.tail = None
                return previous
            while cursor.pointer:
                previous = cursor
                cursor = cursor.pointer
            previous.pointer = None
            return cursor.value
        else:
            raise IndexError("No list to pop from")

    def size(self):
        """Return length of Node chain."""
        if self.tail is None:
            return 0
        cursor = self.tail
        count = 1
        while cursor.pointer:
            count += 1
            cursor = cursor.pointer
        return count

    def search(self, val):
        """Return value if value found in Node chain, otherwise return None."""
        cursor = self.tail
        while cursor:
            if cursor.value == val:
                return cursor
            cursor = cursor.pointer

    def remove(self, node):
        """Remove first instance of val from Node chain."""
        val = node.value
        cursor = self.tail
        if val == cursor.value:
            self.tail = self.tail.pointer
        else:
            previous = cursor
            while cursor:
                if cursor.value == val:
                    previous.pointer = cursor.pointer
                    break
                previous = cursor
                cursor = cursor.pointer

    def display(self):
        """Print and return formatted string displaying Node Chain."""
        cursor = self.tail
        cool_string = u""
        while cursor:
            if isinstance(cursor.value, str):
                cool_string += u"'{}', ".format(cursor.value)
            else:
                cool_string += u"{}, ".format(cursor.value)
            cursor = cursor.pointer
        if cool_string:
            cool_string = u'(' + cool_string[:-2] + u')'
            print(cool_string)
        return cool_string
