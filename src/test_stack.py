# -*- coding=utf-8 -*-
"""Test LinkedList for random inputs."""
import pytest


@pytest.fixture(scope='function')
def empty_list():
    """Fixture of empty stack."""
    from stack import Stack
    return Stack([])


@pytest.fixture(scope='function')
def num_list():
    """Fixture of number list."""
    from stack import Stack
    return Stack([1, 2, 3, 4, 5])


@pytest.fixture(scope='function')
def alpha_list():
    """Fixture of letter stack."""
    from stack import Stack
    return Stack(["a", "b", "c", "d"])


def test_pop_empty(empty_list):
    """Test and empty pop."""
    with pytest.raises(IndexError):
        assert empty_list.pop()


def test_pop(num_list):
    """Test pop function returns the correct value."""
    assert num_list.pop() == 5


def test_pop_tail(num_list):
    """Test that the tail value is reassigned correctly."""
    num_list.pop()
    assert num_list.ll.tail.value == 4


def test_push(alpha_list):
    """Test that tail is set correctly with push."""
    alpha_list.push("word")
    assert alpha_list.ll.tail.value == "word"


def test_push_pointer(alpha_list):
    """Test that the pointer is set correctly with push."""
    alpha_list.push("word")
    assert alpha_list.ll.tail.pointer.value == "d"


def test_push_empty(empty_list):
    """Test that tail is set correctly with push."""
    empty_list.push("word")
    assert empty_list.ll.tail.value == "word"


def test_push_empty_pointer(empty_list):
    """Test that the pointer is set correctly with push."""
    empty_list.push("word")
    assert empty_list.ll.tail.pointer is None
