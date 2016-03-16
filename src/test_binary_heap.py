# -*- coding: utf-8 -*-
"""Test binary heap."""
import pytest


@pytest.fixture(scope='function')
def num_heap():
    from binary_heap import BinaryHeap
    return BinaryHeap([1, 2, 3, 4, 1, 6, 7, 8])

@pytest.fixture(scope='function')
def short_num_heap():
    from binary_heap import BinaryHeap
    return BinaryHeap([1, 2, 3])

@pytest.fixture(scope='function')
def med_num_heap():
    from binary_heap import BinaryHeap
    return BinaryHeap([1, 2, 3, 4, 5])


def test_max_orient(num_heap):
    """Test max organization works."""
    assert num_heap.heap == [8, 7, 6, 4, 1, 3, 1, 2]


def test_max_orient_short(med_num_heap):
    """Test max organization works."""
    assert med_num_heap.heap == [5, 4, 1, 3, 2]
