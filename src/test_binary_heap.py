 # -*- coding: utf-8 -*-
"""Test binary heap."""
import pytest
import heapq


@pytest.fixture(scope='function')
def num_heap():
    """Create a 8 long unordered heap."""
    from binary_heap import BinaryHeap
    return BinaryHeap([1, 2, 3, 4, 1, 6, 7, 8])


@pytest.fixture(scope='function')
def short_num_heap():
    """Create a 3 long heap."""
    from binary_heap import BinaryHeap
    return BinaryHeap([1, 2, 3])


@pytest.fixture(scope='function')
def med_num_heap():
    """Create a 5 long heap."""
    from binary_heap import BinaryHeap
    return BinaryHeap([1, 2, 3, 4, 5])


def test__short_num_heap(short_num_heap):
    assert short_num_heap.heap == [3, 1, 2]


def test_num_heap(num_heap):
    assert num_heap.heap == [8, 7, 6, 3, 1, 2, 4, 1]
