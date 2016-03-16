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

    def _reset(self):
        self._heap = [None]

    @property
    def heap(self):
        return self._heap[1:]

    def __init__(self, values=[]):
        """Heap list initialization."""
        self._reset()
        if isinstance(values, list):
            for item in values:
                if not (isinstance(item, int) or isinstance(item, float)):
                    raise TypeError("Items in list not valid!")
            self._heap = [None] + values
            self.sift()
        else:
            raise TypeError("Please package your item into a list!")

    def sift(self):
        """Rebind the heap with a max to min top-down orientation."""
        run_twice = False
        # Is this the right logic? The world knows, but I never will lel
        while True:
            heap_copy = self._heap
            for (pointer_index, item) in list(enumerate(heap_copy))[::-1]:
                while pointer_index >= 1:

                    print(pointer_index)
                    if not pointer_index:
                        continue
                    if pointer_index == 1:
                        parent_index = sibling_index = None
                    else:
                        if pointer_index % 2:  # if the pointer is odd:
                            sibling_index = pointer_index - 1
                        else:  # if the pointer is even
                            try:
                                sibling_index = pointer_index + 1
                                heap_copy[sibling_index]
                            except IndexError:
                                sibling_index = None

                        parent_index = pointer_index // 2

                    if sibling_index:
                        if heap_copy[pointer_index] > heap_copy[sibling_index]:
                            biggest_index = pointer_index
                        else:
                            biggest_index = sibling_index
                    else:
                        biggest_index = pointer_index

                    if parent_index and heap_copy[parent_index] < heap_copy[biggest_index]:
                        print("TRADING!", heap_copy[parent_index], heap_copy[biggest_index], parent_index, biggest_index)
                        heap_copy[parent_index], heap_copy[biggest_index] = heap_copy[biggest_index], heap_copy[parent_index]

                    print(biggest_index, pointer_index, parent_index)
                    print('w', heap_copy)

                    pointer_index = pointer_index // 2

            if heap_copy == self._heap:
                if run_twice:
                    break
                else:
                    run_twice = True
                self._heap = heap_copy

    def push(self, val):
        """Pushes a value to end of heap while maintaining structure."""
        self._heap.append(val)
        self.sift()

    def pop(self):
        """Remove the head value and maintain structure."""
        self._heap[1] = self._heap[-1]
        self.sift()
