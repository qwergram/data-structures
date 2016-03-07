# -*- coding=utf-8 -*-

class Node(object):

    def __init__(self, value, pointer):
        if pointer and not pointer.isinstance(Node):
            raise TypeError("Pointer must point to a node object")
        self.value = value


class LinkedList(object):

    tail = None

    def __init__(self, initial_values):
        pass

    def insert(self):
        pass

    def pop(self):
        pass

    def size(self):
        pass

    def search(self, val):
        pass

    def remove(self, node):
        pass

    def display(self):
        pass
