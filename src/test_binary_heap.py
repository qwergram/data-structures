# -*- coding: utf-8 -*-
"""Test binary heap."""
import pytest


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


def test_max_orient_order_3(short_num_heap):
    """Test max organization works."""
    assert short_num_heap.heap == [3, 2, 1]


def test_max_orient_non_order_5(num_heap):
    """Test max organization works."""
    assert num_heap.heap == [8, 4, 7, 2, 1, 6, 3, 1]


def test_max_orient_order_6():
    """Test max organization works."""
    from binary_heap import BinaryHeap
    assert BinaryHeap([1, 2, 3, 4, 5, 6]).heap == [6, 5, 3, 4, 2, 1]


def test_max_orient_order_5(med_num_heap):
    """Test max organization works."""
    assert med_num_heap.heap == [5, 4, 3, 1, 2]


def test_max_orient_order_negative_5(med_num_heap):
    """Test max organization works."""
    from binary_heap import BinaryHeap
    assert BinaryHeap([-5, -4, -3, -2, -1]).heap == [-1, -2, -3, -5, -4]


def test_max_orient_non_order_6():
    """Test max organization works."""
    from binary_heap import BinaryHeap
    assert BinaryHeap([93, 482, 53, 23, 67, -4]).heap == [482, 93, 53, 23, 67, -4]


def test_max_orient_pop_order_5(med_num_heap):
    """Test pop works."""
    med_num_heap.pop()
    assert med_num_heap.heap == [4, 2, 3, 1, 2]


def test_max_orient_pop_non_order_8(num_heap):
    """Test pop works."""
    num_heap.pop()
    assert num_heap.heap == [7, 4, 6, 2, 1, 1, 3, 1]


def test_max_orient_push_order_5(med_num_heap):
    """Test push works."""
    med_num_heap.push(93)
    assert med_num_heap.heap == [93, 4, 5, 1, 2, 3]


def test_max_orient_push_non_order_8(num_heap):
    """Test push works."""
    num_heap.push(93)
    assert num_heap.heap == [93, 8, 7, 4, 1, 6, 3, 1, 2]
