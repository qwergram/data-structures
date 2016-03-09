# -*- coding=utf-8 -*-
"""Test Dll for random inputs."""
import pytest

NODE_TEST_ITEMS = [
    (object,),
    (235,),
    ("asdf",),
    (['asdf', 'asdf'],),
    (list(range(0, 75)),),
    [],
    {},
]


@pytest.mark.parametrize('item', NODE_TEST_ITEMS)
def test_dll_node(item):
    """Test that DLLNode initializes correctly."""
    from dll import DllNode
    assert DllNode(item).value == item


@pytest.mark.parametrize('item', NODE_TEST_ITEMS)
def test_linkedlist_insert_integer(item):
    """Test Dll insert command works correctly."""
    from dll import Dll
    input_ = [1, 2]
    dll_instance = Dll(input_)
    dll_instance.insert(item)
    assert dll_instance.tail.pointer.pointer.value == item

#
