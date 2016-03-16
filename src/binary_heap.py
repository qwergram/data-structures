# -*- coding: utf-8 -*-
"""Implementing a binary heap data structure."""


class BinaryHeap(object):
    """Define a BinaryHeap object."""

    def _reset(self):
        self.heap = []

    def __init__(self, values=[], organization='max'):
        """Heap list initialization."""
        self._reset()
        if organization.lower() == 'max':
            self._orient = self._max_orient
        elif organization.lower() == 'min':
            self._orient = self._min_orient
        else:
            raise ValueError('oraganization argument invalid')
        if isinstance(values, list):
            self.heap = values
            self._orient()
            # for value in values:
                # self.push(value)
        else:
            raise TypeError("Please package your item into a list!")

    def _max_orient(self):
        """Rebind the heap with a max to min top-down orientation."""
        # import pdb; pdb.set_trace()
        length = len(self.heap)
        while True:
            start_heap = self.heap
            for cursor in range(length):
                # print(cursor)
                if cursor == 0:
                    left = 1
                    right = 2
                else:
                    left = cursor * 2
                    right = (cursor * 2) + 1
                try:
                    print(cursor + 1)
                    print(left + 1)
                    print(right + 1)
                    print()
                except IndexError:
                    pass

            break

        # while True:
        #     start_heap = self.heap
        #     for cur in range(1, length):
        #         cur = length - cur
        #         print(self.heap)
        #
        #         if cur % 2 == 0:
        #             i = cur // 2
        #         else:
        #             i = (cur // 2) + 1
        #
        #         print(i)
        #         print("i c i c")
        #         print(i, cur, self.heap[i], self.heap[cur])
        #         if self.heap[i] < self.heap[cur]:
        #             self.heap[i], self.heap[cur] = self.heap[cur], self.heap[i]
        #     if start_heap == self.heap:
        #         break

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


if __name__ == "__main__":
    b = BinaryHeap([1,2,3,4,5])
    print(b.heap)
