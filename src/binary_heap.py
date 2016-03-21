# -*- coding: utf-8 -*-
"""Implementing a binary heap data structure."""


class BinaryHeap(object):
    """Define a  max BinaryHeap object."""

    def __init__(self, value=[]):
        """Initialize heap object."""
        self.heap = []
        self.push(value)

    def _restructure(self):
        """Maintain structure of heap to max."""
        if len(self.heap) > 1:  # Solves 0 and 1 case THIS IS GOOD'
            biggest = self.heap[-1]

            while biggest != self.heap[0]:

                for i, value in enumerate(self.heap):
                    if i == 0:
                        continue
                    if biggest < value:
                        biggest = value
                    try:
                        if value < self.heap[i * 2]:
                            self.heap[i], self.heap[2 * i] = self.heap[i * 2], value  # NOQA
                        if value < self.heap[(i * 2) + 1]:
                            self.heap[i], self.heap[(2 * i) + 1] = self.heap[(i * 2) + 1], value   # NOQA
                    except IndexError:
                        break
                if self.heap[0] < self.heap[1]:
                    biggest = self.heap[-1]
                    self.heap[0], self.heap[1] = self.heap[1], self.heap[0]
                else:
                    break

    def push(self, value):
        """Push a value into the heap."""
        if hasattr(value, '__iter__'):
            for index in value:
                self.heap.append(index)
                self._restructure()
        else:
            self.heap.append(value)
            self._restructure()

    def pop(self):
        """Return the initial value of the heap."""
        try:
            removed = self.heap[0]
            self.heap = self.heap[1:]
            self._restructure()
            return removed
        except IndexError:
            return None
