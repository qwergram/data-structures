# -*- coding: utf-8 -*-
"""Test for deque list."""
import pytest


@pytest.fixture(scope='function')
def alpha_list():
    """Create a Node Chain with letters."""
    from deque import Deque
    return Deque('a b c d e f'.split())


@pytest.fixture(scope='function')
def empty_list():
    """Create a Node Chain with nothing."""
    from deque import Deque
    return Deque([])


def test_deque_append(alpha_list):
    """Test the tail if the enqueue is working correctly."""
    alpha_list.append("g")
    assert alpha_list.dll.tail.value == "g"


def test_deque_append_pointer_next(alpha_list):
    """Test the tail next pointer if the enqueue is working correctly."""
    alpha_list.append("g")
    assert alpha_list.dll.tail.next is None


def test_deque_append_pointer_prev(alpha_list):
    """Test the tail prev pointer if the enqueue is working correctly."""
    alpha_list.append("g")
    assert alpha_list.dll.tail.prev.value == "f"


def test_deque_size_long():
    """Test Deque.size for proper length return."""
    from deque import Deque
    input_ = list(range(75))
    deque_instance = Deque(input_)
    assert deque_instance.size() == len(input_)


def test_deque_size_empty():
    """Test Queue.size for proper length return."""
    from deque import Deque
    input_ = []
    deque_instance = Deque(input_)
    assert deque_instance.size() == len(input_)


def test_deque_peek(alpha_list):
    """Test peek functionality returns head."""
    assert alpha_list.peek() == 'f'


def test_deque_peek_emtpy(empty_list):
    """Test peek functionality returns None."""
    assert empty_list.peek() is None


def test_deque_peekleft(alpha_list):
    """Test peek functionality returns head."""
    assert alpha_list.peekleft() == 'a'


def test_deque_peekleft_emtpy(empty_list):
    """Test peek functionality returns None."""
    assert empty_list.peekleft() is None


def test_deque_appendleft(alpha_list):
    """Test the tail if the enqueue is working correctly."""
    alpha_list.appendleft("g")
    assert alpha_list.dll.head.value == "g"


def test_deque_appendleft_pointer_next(alpha_list):
    """Test the tail next pointer if the enqueue is working correctly."""
    alpha_list.appendleft("g")
    assert alpha_list.dll.head.next.value == "a"


def test_deque_appendleft_pointer_prev(alpha_list):
    """Test the tail prev pointer if the enqueue is working correctly."""
    alpha_list.appendleft("g")
    assert alpha_list.dll.head.prev is None


def test_deque_pop_return(alpha_list):
    """Test the pop return if the pop is working correctly."""
    assert alpha_list.pop().value == 'f'


def test_deque_pop_head(alpha_list):
    """Test the head if the pop is working correctly."""
    alpha_list.pop()
    assert alpha_list.dll.head.value == 'a'


def test_deque_pop_tail(alpha_list):
    """Test the tail if the pop is working correctly."""
    alpha_list.pop()
    assert alpha_list.dll.tail.value == 'e'


def test_deque_pop_empty(empty_list):
    """Test if IndexError is raised when popping an empty list."""
    with pytest.raises(IndexError):
        empty_list.pop()


def test_deque_popleft_return(alpha_list):
    """Test the return value if the popleft is working correctly."""
    assert alpha_list.popleft().value == 'a'


def test_deque_popleft_head(alpha_list):
    """Test the head if the popleft is working correctly."""
    alpha_list.popleft()
    assert alpha_list.dll.head.value == 'b'


def test_deque_popleft_tail(alpha_list):
    """Test the tail if the popleft is working correctly."""
    alpha_list.popleft()
    assert alpha_list.dll.tail.value == 'f'


def test_deque_popleft_empty(empty_list):
    """Test if IndexError is raised when poplefting an empty list."""
    with pytest.raises(IndexError):
        empty_list.popleft()