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


@pytest.fixture(scope='function')
def alpha_list():
    """Create a Node Chain with letters"""
    from dll import DoublyLinkedList
    return DoublyLinkedList('a b c d e f'.split())


@pytest.fixture(scope='function')
def num_list():
    """Create a Node Chain with numbers"""
    from dll import DoublyLinkedList
    return DoublyLinkedList([1, 2, 3])


@pytest.fixture(scope='function')
def empty_list():
    """Create a Node Chain with nothing"""
    from dll import DoublyLinkedList
    return DoublyLinkedList([])


@pytest.mark.parametrize('item', NODE_TEST_ITEMS)
def test_dll_node(item):
    """Test that DLLNode initializes correctly."""
    from dll import Node
    assert Node(item, None, None).value == item


def test_dll_initialize_head(num_list):
    """Test if the head is initializing correctly"""
    assert num_list.head.value == 1


def test_dll_initialize_tail(num_list):
    """Test if the tail is initializing correctly"""
    assert num_list.tail.value == 3


def test_dll_append(alpha_list):
    """Test the tail if the append is working correctly"""
    alpha_list.append("g")
    assert alpha_list.tail.value == "g"


def test_dll_append_pointer_next(alpha_list):
    """Test the tail next pointer if the append is working correctly"""
    alpha_list.append("g")
    assert alpha_list.tail.next is None


def test_dll_append_pointer_prev(alpha_list):
    """Test the tail prev pointer if the append is working correctly"""
    alpha_list.append("g")
    assert alpha_list.tail.prev.value == "f"


def test_dll_insert(num_list):
    """Test the head if the insert is working correctly"""
    num_list.insert(0)
    assert num_list.head.value == 0


def test_dll_insert_pointer_next(num_list):
    """Test the head next pointer if the insert is working correctly"""
    num_list.insert(0)
    assert num_list.head.next.value == 1


def test_dll_insert_pointer_prev(num_list):
    """Test the head prev pointer if the insert is working correctly"""
    num_list.insert(0)
    assert num_list.head.prev is None


def test_dll_pop_return(alpha_list):
    """Test the pop return if the pop is working correctly"""
    assert alpha_list.pop().value == 'a'


def test_dll_pop_head(alpha_list):
    """Test the head if the pop is working correctly"""
    alpha_list.pop()
    assert alpha_list.head.value == 'b'


def test_dll_pop_tail(alpha_list):
    """Test the tail if the pop is working correctly"""
    alpha_list.pop()
    assert alpha_list.tail.value == 'f'


def test_dll_pop_empty(empty_list):
    """Test if IndexError is raised when popping an empty list"""
    with pytest.raises(IndexError):
        empty_list.pop()


def test_dll_shift_return(alpha_list):
    assert alpha_list.shift().value == 'f'


def test_dll_shift_head(alpha_list):
    alpha_list.shift()
    assert alpha_list.head.value == 'a'


def test_dll_shift_tail(alpha_list):
    alpha_list.shift()
    assert alpha_list.tail.value == 'e'


def test_dll_shift_empty(empty_list):
    with pytest.raises(IndexError):
        empty_list.shift()


def test_dll_remove_empty(empty_list):
    with pytest.raises(ValueError):
        empty_list.remove("value_not_there")


def test_dll_remove_like_pop(alpha_list):
    alpha_list.remove('a')
    assert alpha_list.head.value == 'b'


def test_dll_remove_like_shift(alpha_list):
    alpha_list.remove('f')
    assert alpha_list.tail.value == 'e'


def test_dll_remove_central_prev_pointers(alpha_list):
    alpha_list.remove('c')
    assert alpha_list.tail.prev.prev.prev.value == 'b'


def test_dll_remove_central_next_pointers(alpha_list):
    alpha_list.remove('c')
    assert alpha_list.head.next.next.value == 'd'

# @pytest.mark.parametrize('item', NODE_TEST_ITEMS)
# def test_linkedlist_insert_integer(item):
#     """Test Dll insert command works correctly."""
#     from dll import Dll
#     input_ = [1, 2]
#     dll_instance = Dll(input_)
#     assert dll_instance.tail.value == 2
#     assert dll_instance.tail.pointer.value == 1
#     assert dll_instance.tail.previous is None
#     dll_instance.insert(item)
#     assert dll_instance.tail.pointer.pointer.value == item
#     assert dll_instance.tail.pointer.pointer.previous.value == 1
