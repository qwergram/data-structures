# -*- coding=utf-8 -*-

class Node(object):

    def __init__(self, value, pointer):
        if pointer is None or isinstance(pointer, Node):
            self.pointer = pointer
        else:
            raise TypeError("Pointer must point to a node object")

        self.value = value


class LinkedList(object):

    tail = None

    def __init__(self, initial_values):
        for item in initial_values:
            self.tail = Node(item, self.tail)

    def insert(self, val):
        self.tail = Node(value, self.tail)

    def pop(self):
        cursor = self.tail
        previous = None

        while cursor.pointer:
            previous = cursor
            cursor = cursor.pointer

        previous.pointer = None

        return cursor


    def size(self):

        cursor = self.tail
        count = 1

        while cursor.pointer:
            count += 1
            cursor = cursor.pointer

        return count

    def search(self, val):
        cursor = self.tail

        while cursor:
            if cursor.value == val:
                return cursor
            cursor = cursor.pointer


    def remove(self, node):
        



    def display(self):
        pass
