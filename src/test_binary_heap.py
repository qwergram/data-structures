# -*- coding: utf-8 -*-
"""Test binary heap."""
import pytest


def test_max_orient():
    """Test max organization works."""
    from binary_heap import BinaryHeap
    list_ = [1, 2, 3, 4, 1, 6, 7, 8]
    heap_instance = BinaryHeap(list_)
    assert heap_instance.heap == [8, 7, 6, 4, 1, 3, 2, 1]


def test_max_orient_5():
    """Test max organization works."""
    from binary_heap import BinaryHeap
    list_ = [1, 2, 3]
    heap_instance = BinaryHeap(list_)
    assert heap_instance.heap == [3, 2, 1]