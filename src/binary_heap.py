# -*- coding: utf-8 -*-
"""Implementing a binary heap data structure."""


class BinaryHeap(object):
    """Define a BinaryHeap object."""

    heap = [None]

    def __init__(self, values=[], organization='max'):
        """Heap list initialization."""
        if organization.lower() == 'max':
            self._orient = self._max_orient
        elif organization.lower() == 'min':
            self._orient = self._min_orient
        else:
            raise ValueError('oraganization argument invalid')
        if isinstance(values, list):
            for value in values:
                self.push(value)
        else:
            raise TypeError("Please package your item into a list!")

    def _max_orient(self):
        """Rebind the heap with a max to min top-down orientation."""
        length = len(self.heap) - 1
        while True:
            start_heap = self.heap
            for cur in range(2, length):
                cur = length - cur
                # assert type(self.heap[cur]) == int, cur
                # if cur == 0:
                #     break
                i = cur // 2
                if self.heap[i] < self.heap[cur]:
                    self.heap[i], self.heap[cur] = self.heap[cur], self.heap[i]
            if start_heap == self.heap:
                break

    def _min_orient(self):
        """Rebind the heap with a min to max top-down orientation."""
        length = len(self.heap) - 1
        while True:
            start_heap = self.heap
            for cur in range(1, length):
                cur = length - cur
                if cur == 0:
                    break
                i = cur // 2
                if self.heap[i] > self.heap[cur]:
                    self.heap[i], self.heap[cur] = self.heap[cur], self.heap[i] 
            if start_heap == self.heap:
                break

    def push(self, val):
        """Pushes a value to end of heap while maintaining structure."""
        self.heap.append(val)
        self._orient()

    def pop(self):
        """Remove the head value and maintain structure."""
        self.heap[0] = self.heap[-1]
        self._orient()
