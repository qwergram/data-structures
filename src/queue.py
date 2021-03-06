# -*- coding: utf-8 -*-
"""Create a Queue object that fits the definition defined here.

http://www.princeton.edu/~achaney/tmve/wiki100k/docs/Queue_(data_structure).html
http://ls.pwd.io/2014/08/singly-and-doubly-linked-lists-in-python/
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
    """Classify a NodeObject that points to two different objects."""

    def __init__(self, value, nxt, prev):
        """Initialize node."""
        self.value = value
        self.next = nxt
        self.prev = prev


class Queue(object):
    """Define Queue object.

    Classify a new object that resembles a LinkedList following
    a first in first out logic.
    """

    head = None
    tail = None

    def __init__(self, values=[]):
        """Initalize the queue chain."""
        if isinstance(values, list):
            for value in values:
                self.enqueue(value)
        else:
            raise TypeError("Please package your item into a list!")

    def enqueue(self, value):
        """Enqueue a value to the tail of the linked list."""
        new_node = Node(value, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self, value):
        """Dequeue the specified item from the node chain."""
        current_node = self.head
        previous_node = None
        if self.tail is not None and self.tail.value == value:
            self.tail = self.tail.prev
            self.tail.next = None
        elif self.head is not None and self.head.value == value:
            self.head = self.head.next
            self.head.prev = None
        else:
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

    def size(self):
        """Return the size of the queue."""
        if self.tail is None:
            return 0
        cursor = self.tail
        count = 1
        while cursor.prev:
            count += 1
            cursor = cursor.prev
        return count

    def peek(self):
        """Return next item in queue without removing it."""
        if self.head:
            return self.head.value
