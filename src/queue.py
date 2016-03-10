# -*- coding: utf-8 -*-
"""Create a Queue object that fits the definition defined here:
    http://www.princeton.edu/~achaney/tmve/wiki100k/docs/Queue_(data_structure).html

    It should have the following methods:

    .enqueue(value): Add a value to the queue
    .dequeue(value): Remove a value from the queue and return the value
        - If empty, raise an Exception
    .peek(): Return the next value
        - If empty, return None
    .size(): Check the size of the queue

    This queue follows a logic of first in, first out.
"""

class Node(object):

    def __init__(self, value, next, prev):

        # Require the user to explicitly state the pointers
        # as per zen of python line 2 (python -m this)
        self.value = value
        self.next = next  # In other words: pointer towards the tail
        self.prev = prev  # In other words: previous towards the head


class Queue(object):

    head = None
    tail = None

    def dequeue(self, value):
        """Dequeue the specified item from the node chain and rebind the Nodes agian"""
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.value == value:
                if previous_node is not None:
                    previous_node.next = current_node.next
                    previous_node.next.prev = previous_node
                else:
                    self.head = current_node.next
                break
            previous_node = current_node
            current_node = current_node.next
        else:
            raise ValueError("Item was not found in list!")
