# -*- coding=utf-8 -*-
"""Test LinkedList for random inputs."""
import pytest

NODE_TEST_ITEMS = [
    (object,),
    (235,),
    ("asdf",),
    (['asdf', 'asdf'],),
    (list(range(0, 75)),),
]


@pytest.mark.parametrize('item', NODE_TEST_ITEMS)
def test_dll_node(item):
    """Test that DLLNode initializes correctly."""
    from dll import DllNode
    assert DllNode(item).value == item
