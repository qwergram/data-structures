# -*- coding=utf-8 -*-
"""Test LinkedList for random inputs."""
import pytest


@pytest.fixture(scope='function')
def stack_push():
    """Test fixture for stack push method."""
    from stack import Stack
    input_ = ['sad']
    stack_instance = Stack(input_)
    stack_instance.push('happy')
    return stack_instance


def test_stack_push_tail(stack_push):
    """Test Stack. push method."""
    assert stack_push.tail.value == 'happy'


def test_stack_push_pointer(stack_push):
    """Test Stack. push method."""
    assert stack_push.tail.pointer.value == 'sad'


def test_stack_pop():
    """Test Stack.pop method."""
    from stack import Stack
    input_ = [1]
    stack_instance = Stack(input_)
    assert stack_instance.pop() == 1
