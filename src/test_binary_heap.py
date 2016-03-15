# -*- coding: utf-8 -*-
"""Test binary heap."""
import pytest


def test_max_orient():
    """Test max organization works."""
    from binary_heap import BinaryHeap
    list_ = [1, 2, 3, 4, 1, 6, 7, 8]
    heap_instance = BinaryHeap(list_)
    assert heap_instance.heap == [None, 8, 7, 6, 4, 1, 3, 1, 2]
