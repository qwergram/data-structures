# -*- coding: utf-8 -*-
"""Create a priority queue list."""

class PrioityQ(object):

    priority_queue = {}

    def __init__(self, values=[]):
        """Initalize the queue chain."""
        if isinstance(values, list):
            try:
                for value, priority in values:
                    if not isinstance(prioirity, int):
                        raise TypeError("Please set the priority type to integer")
                    self.insert(value, priority)
            except ValueError:
                raise TypeError("Please package your priority into tuples!")
        else:
            raise TypeError("Please package your item into a list!")


    def insert(self, value, priority=2):
        """Insert value into Priority Queue based on Priority"""
        if priority in self.priority_queue:
            self.priority_queue[priority].append(value)
        else:
            self.priority_queue[priority] = [value]


PrioityQ([("do things", 0)])
