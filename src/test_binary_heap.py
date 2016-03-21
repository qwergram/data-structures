# -*- coding: utf-8 -*-
"""Test binary heap."""
import pytest


@pytest.fixture(scope='function')
def binary_heap_object():
    """Create a single item test."""
    from binary_heap import BinaryHeap
    return BinaryHeap()


@pytest.fixture(scope='function')
def big_binary_heap_object():
    """Create a multiple level heap object."""
    from binary_heap import BinaryHeap
    obj = BinaryHeap()
    for x in range(1, 9):
        obj.push(x)
    return obj


def test_iterable_initation():
    """Inititiate an iterable."""
    from binary_heap import BinaryHeap
    assert BinaryHeap([1, 2, 3, 4, 5, 6, 7, 8]).heap == [8, 7, 4, 6, 1, 3, 2, 5]


def test_pop_empty():
    """Pop and empty list."""
    from binary_heap import BinaryHeap
    instance_binheap = BinaryHeap()
    assert instance_binheap.pop() is None


def test_pop_one():
    """Pop a list of one."""
    from binary_heap import BinaryHeap
    instance_binheap = BinaryHeap(1)
    assert instance_binheap.pop() == 1


def test_pop_one_heap():
    """Pop a list of one and see what is left in the heap."""
    from binary_heap import BinaryHeap
    instance_binheap = BinaryHeap(1)
    instance_binheap.pop()
    assert instance_binheap.heap == []


def test_binary_heap_object(binary_heap_object):
    """Test a single push."""
    binary_heap_object.push(1)
    assert binary_heap_object.heap == [1]


def test_binary_heap_object_2(binary_heap_object):
    """Test a single push."""
    binary_heap_object.push(1)
    binary_heap_object.push(2)
    assert binary_heap_object.heap == [2, 1]


def test_big_binary_heap_object(big_binary_heap_object):
    """Test a restructure heap values."""
    assert big_binary_heap_object.heap == [8, 7, 4, 6, 1, 3, 2, 5]


def test_big_object_pop(big_binary_heap_object):
    """Test pop."""
    assert big_binary_heap_object.pop() == 8


def test_big_object_heap_restructure(big_binary_heap_object):
    """Test restructure post pop."""
    big_binary_heap_object.pop()
    assert big_binary_heap_object.heap == [7, 6, 4, 5, 3, 2, 1]
