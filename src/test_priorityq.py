# -*- coding:utf-8 -*-
"""Test ptiority queue."""
import pytest


@pytest.fixture(scope='function')
def empty_dict():
    """Test an empty dictionary."""
    from priorityq import PriorityQ
    return PriorityQ()


@pytest.fixture(scope='function')
def alpha_list():
    """Create a dict of letters with priorities."""
    from priorityq import PriorityQ
    return PriorityQ([('a', 1), ('b', 1), ('c', 2), ('d', 3), (3, 1)])


def test_bad_init():
    """Test a bad tuple init."""
    from priorityq import PriorityQ
    with pytest.raises(TypeError):
        PriorityQ("helllo")


def test_bad_tuple_formation():
    """Test a bad tuple part 2."""
    from priorityq import PriorityQ
    with pytest.raises(TypeError):
        PriorityQ([('fuck', 'this', 'shit')])


def test_pop_empty(empty_dict):
    """Test if you can pop an empty piority queue."""
    with pytest.raises(IndexError):
        empty_dict.pop()


def test_pop_alpha(alpha_list):
    """Test a well formatted list of tuples."""
    assert alpha_list.pop() == 'a'


def test_peek_empty(empty_dict):
    """Test if you can peek an empty piority queue."""
    assert empty_dict.peek() is None


def test_peek_alpha(alpha_list):
    """Test a well formatted list of tuples."""
    assert alpha_list.peek() == 'a'


def test_insert_empty(empty_dict):
    """Test if you can insert an empty piority queue."""
    empty_dict.insert([])
    assert empty_dict.priority_queue.get(2)[0] == []


def test_insert_pop_empty(empty_dict):
    """Test if you can insert an empty piority queue."""
    empty_dict.insert([])
    empty_dict.pop()
    assert empty_dict.priority_queue.get(2) is None
    with pytest.raises(IndexError):
        empty_dict.pop()


def test_insert_alpha(alpha_list):
    """Test if you can insert an empty piority queue."""
    alpha_list.insert('hello', 1)
    assert alpha_list.priority_queue.get(1)[3] == 'hello'


def pop_on_empty_queue(empty_dict):
    """Test if priorityq can pop from multipl priorty levels."""
    empty_dict.insert(1, "Server broken")
    empty_dict.insert(5, "Feed children")
    assert empty_dict.pop() == "Server broken"
    assert empty_dict.pop() == "Feed children"
