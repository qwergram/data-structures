# -*- coding: utf-8 -*-
"""Implementing a binary heap data structure."""


class BinaryHeap(object):
    """Define a BinaryHeap object.

        There are multiple definitions/variations of a BinaryHeap according to
        Wikipedia. (https://en.wikipedia.org/wiki/Binary_heap) so there were
        multiple algorithms to choose from. The algorithm or variation that this
        heap follows is the default definition which is what is dicussed on the
        page linked.

    """

    heap = []

    @property
    def length(self):
        return len(self.heap)

    def __init__(self, values=[]):
        """Heap list initialization."""
        if isinstance(values, list):
            for item in values:
                if not (isinstance(item, int) or isinstance(item, float)):
                    raise TypeError("Items in list not valid!")
                self.push(item)
        else:
            raise TypeError("Please package your item into a list!")

    def sift(self, startpos, pos):
        """Rebind the heap with a max to min top-down orientation."""
        newitem = self.heap[pos]
        # This is from the module heapq
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = self.heap[parentpos]
            if newitem > parent:
                self.heap[pos] = parent
                pos = parentpos
                continue
            break
        self.heap[pos] = newitem

    def push(self, val):
        """Pushes a value to end of self.heap while maintaining structure."""
        self.heap.append(val)
        self.sift(0, self.length - 1)

    def pop(self):
        """Remove the head value and maintain structure."""
        self.heap[1] = self.heap[-1]
        self.sift(0, self.length - 1)
