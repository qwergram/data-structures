# -*- coding: utf-8 -*-
"""Create a priority queue list."""


class PriorityQ(object):

    def __init__(self, values=[]):
        """Initalize the queue chain."""
        self._reset()
        if isinstance(values, list):
            try:
                for value, priority in values:
                    self.insert(value, priority)
            except ValueError:
                raise TypeError("Please package your priority into tuples!")
        else:
            raise TypeError("Please package your item into a list!")

    def insert(self, value, priority=2):
        """Insert value into Priority Queue based on Priority."""
        if not isinstance(priority, int):
            raise TypeError('Priority must be an integer')
        if priority in self.priority_queue:
            self.priority_queue[priority].append(value)
        else:
            self.priority_queue[priority] = [value]

    def pop(self):
        print(self.priority_queue)
        if len(self.priority_queue.values()) != 0:
            highest = sorted(self.priority_queue)[0]
            to_pop = self.priority_queue[highest][0]
            self.priority_queue[highest] = self.priority_queue[highest][1:]
            if not len(self.priority_queue[highest]):
                del self.priority_queue[highest]
            return to_pop
        else:
            raise IndexError("Hey, the queue is empty")

    def peek(self):
        try:
            highest = sorted(self.priority_queue)[0]
            to_pop = self.priority_queue[highest][0]
            return to_pop
        except IndexError:
            return None

    def _reset(self):
        self.priority_queue = {}
