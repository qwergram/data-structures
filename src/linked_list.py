# -*- coding=utf-8 -*-
"""Hold sample code for number of classic data structures implemented in Python"""


class Node(object):
    """A class inheriting object that holds a value and pointer"""

    def __init__(self, value, pointer):
        """Build a Node object with specified value and pointer"""
        if pointer is None or isinstance(pointer, Node):
            self.pointer = pointer
        else:
            raise TypeError("Pointer must point to a node object")
        self.value = value


class LinkedList(object):
    """A class wrapper with Node linking methods"""
    tail = None

    def __init__(self, initial_values):
        """Build a LinkedList of specified Nodes"""
        for item in initial_values:
            self.tail = Node(item, self.tail)

    def insert(self, val):
        """Insert value into Linked Node list"""
        self.tail = Node(val, self.tail)

    def pop(self):
        """Return and remove head from Linked Node list"""
        cursor = self.tail
        previous = None
        while cursor.pointer:
            previous = cursor
            cursor = cursor.pointer
        previous.pointer = None
        return cursor

    def size(self):
        """Return length of Node chain"""
        cursor = self.tail
        count = 1
        while cursor.pointer:
            count += 1
            cursor = cursor.pointer
        return count

    def search(self, val):
        """Return value if value found in Node chain, otherwise returns None"""
        cursor = self.tail
        while cursor:
            if cursor.value == val:
                return cursor
            cursor = cursor.pointer

    def remove(self, val):
        """Remove first instance of val from Node chain"""
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
        """Print and return formatted string displaying Node Chain"""
        cursor = self.tail
        cool_string = u"("
        while cursor:
            if isinstance(cursor.value, str):
                cool_string += u"'{}', ".format(cursor.value)
            else:
                cool_string += u"{}, ".format(cursor.value)
            cursor = cursor.pointer
        cool_string = cool_string[:-2] + u')'
        print(cool_string)
        return cool_string
