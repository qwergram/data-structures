# -*- coding: utf-8 -*-
"""Implementing a binary heap data structure."""


class BinaryHeap(object):
    """Define a  max BinaryHeap object."""

    def __init___(self):
        """Initialize heap object."""
        self.heap = []

    def restructure(self):
        """Maintain structure of heap to max."""
        if len(self.heap) > 1:  # Solves 0 and 1 case THIS IS GOOD'
            biggest = self.heap[-1]
            while biggest != self.heap[0]:
                for i, value in enumerate(self.heap):
                    if biggest < value:
                        biggest = value
                    try:
                        if value < self.heap[i * 2]:
                            self.heap[i], self.heap[2 * i] = self.heap[i * 2], value
                        if value < self.heap[(i * 2) + 1]:
                            self.heap[i], self.heap[(2 * i) + 1] = self.heap[(i * 2) + 1], value
                    except IndexError:
                        break

    def push(self, value):
        """Push a value into the heap."""
        self.heap.append(value)
        self.restructure()

    def pop(self):
        """Return the initial value of the heap."""
        removed = self.heap[0]
        self.heap = self.heap[1:]
        self.restructure()
        return removed
