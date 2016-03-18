# -*- coding: utf-8 -*-
"""Doubl linked List implementation."""


class Node(object):
    """Creates a node object."""

    def __init__(self, value, next, prev):
        """Initalize Node Object."""
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList(object):
    """Define a double pointered list."""

    # It was quite difficult trying to solve this problem, so I got some help
    # with my logic from the following site:
    # http://ls.pwd.io/2014/08/singly-and-doubly-linked-lists-in-python/

    head = None
    tail = None

    def __init__(self, values):
        """Accept a list of values and generate a chain of Nodes using those values."""
        if isinstance(values, list):
            for value in values:
                self.append(value)
        else:
            raise TypeError("Please package your item into a list!")

    def append(self, value):
        """Append a value to the tail of the linked list."""
        new_node = Node(value, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, value):
        """Insert a value to the head of the linked list."""
        new_node = Node(value, None, None)
        if self.head is None: 
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node

    def pop(self):
        """Remove the head of the chain and return the Node."""
        if self.head is None:
            raise IndexError("Cannot execute on an empty list!")
        elif self.head.next is None:
            old_head = self.head
            self.head = self.tail = None
            return old_head
        else:
            old_head = self.head
            new_head = self.head.next
            new_head.prev = None
            self.head = new_head
            old_head.next = None
            old_head.prev = None
            return old_head

    def shift(self):
        """Remove the tail of the chain and return the Node."""
        if self.head is None:
            raise IndexError("Cannot execute an empty list!")
        elif self.head.next is None:
            old_head = self.head
            self.head = self.tail = None
            return old_head
        else:
            old_tail = self.tail
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail = new_tail
            old_tail.next = None
            old_tail.prev = None
            return old_tail

    def remove(self, value):
        """Remove the specified item from the node chain and rebind the Nodes again."""
        if self.tail is not None and self.tail.value == value:
            self.shift()
        elif self.head is not None and self.head.value == value:
            self.pop()
        else:
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
