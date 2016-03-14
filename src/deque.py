# -*- coding: utf-8 -*-
"""Create a deque list."""
import dll


class Deque(object):
    """Deque class initiailed."""

    def __init__(self, values=[]):
        """Deque initialized with a composition of DLL."""
        self.dll = dll.DoublyLinkedList(values)

    def append(self, val):
        """Return a list with val appended to tail."""
        self.dll.append(val)

    def appendleft(self, val):
        """Append value to head."""
        self.dll.insert(val)

    def pop(self):
        """Return and remove the tail value."""
        return self.dll.shift()

    def popleft(self):
        """Return and remove the head value."""
        return self.dll.pop()

    def peek(self):
        """Return the value at the tail of the list."""
        if self.dll.tail:
            return self.dll.tail.value

    def peekleft(self):
        """Return the value at the head of the lsit."""
        if self.dll.head:
            return self.dll.head.value

    def size(self):
        """Return the number of nodes in the list."""
        if self.dll.tail is None:
            return 0
        cursor = self.dll.tail
        count = 1
        while cursor.prev:
            count += 1
            cursor = cursor.prev
        return count
