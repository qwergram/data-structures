# -*- coding: utf-8 -*-
"""Test for queue list."""
import pytest


@pytest.fixture(scope='function')
def alpha_list():
    """Create a Node Chain with letters."""
    from queue import Queue
    return Queue('a b c d e f'.split())


@pytest.fixture(scope='function')
def empty_list():
    """Create a Node Chain with nothing."""
    from queue import Queue
    return Queue([])


def test_queue_dequeue_empty(empty_list):
    """Test if ValueError is raised when removing item that doesn't exist."""
    with pytest.raises(ValueError):
        empty_list.dequeue("value_not_there")


def test_queue_dequeue_like_pop(alpha_list):
    """Test the head if dequeue is working correctly."""
    alpha_list.dequeue('a')
    assert alpha_list.head.value == 'b'


def test_queue_dequeue_like_shift(alpha_list):
    """Test the tail if dequeue is working correctly."""
    alpha_list.dequeue('f')
    assert alpha_list.tail.value == 'e'


def test_queue_dequeue_central_prev_pointers(alpha_list):
    """Test the pointer if dequeue is working correctly."""
    alpha_list.dequeue('c')
    assert alpha_list.tail.prev.prev.prev.value == 'b'


def test_queue_dequeue_central_next_pointers(alpha_list):
    """Test the pointer if dequeue is working correctly."""
    alpha_list.dequeue('c')
    assert alpha_list.head.next.next.value == 'd'


def test_queue_enqueue(alpha_list):
    """Test the tail if the enqueue is working correctly."""
    alpha_list.enqueue("g")
    assert alpha_list.tail.value == "g"


def test_queue_enqueue_pointer_next(alpha_list):
    """Test the tail next pointer if the enqueue is working correctly."""
    alpha_list.enqueue("g")
    assert alpha_list.tail.next is None


def test_queue_enqueue_pointer_prev(alpha_list):
    """Test the tail prev pointer if the enqueue is working correctly."""
    alpha_list.enqueue("g")
    assert alpha_list.tail.prev.value == "f"
