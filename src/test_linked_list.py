# -*- coding=utf-8 -*-
"""Test LinkedList for random inputs."""
import pytest


def test_linkedlist_tail_default():
    """Test LinkedList contstructor for functionality."""
    from linked_list import LinkedList
    assert LinkedList.tail is None


def test_linkedlist_construct_empty_list():
    """Test LinkedList insert command works with empty list."""
    from linked_list import LinkedList
    input_ = []
    linked_list_instance = LinkedList(input_)
    assert linked_list_instance.tail is None


def test_linkedlist_construct_integer():
    """Test LinkedList insert command works with empty list."""
    from linked_list import LinkedList
    input_ = 5
    linked_list_instance = LinkedList(input_)
    assert linked_list_instance.tail.value == 5


def test_linkedlist_constructor_list_isnode():
    """Test LinkedList contstructor for functionality."""
    from linked_list import LinkedList, Node
    input_ = [1, 2]
    linked_list_instance = LinkedList(input_)
    assert isinstance(linked_list_instance.tail, Node)


def test_linkedlist_constructor_nodeval():
    """Test LinkedList contstructor for functionality."""
    from linked_list import LinkedList, Node
    input_ = [1, 2]
    ll_inst = LinkedList(input_)
    assert ll_inst.tail.pointer.value == Node(2, Node(1, None)).pointer.value


def test_linkedlist_constructor_nodeterm():
    """Test LinkedList contstructor for functionality."""
    from linked_list import LinkedList
    input_ = [1, 2]
    linked_list_instance = LinkedList(input_)
    assert linked_list_instance.tail.pointer.pointer is None


def test_linkedlist_insert_integer():
    """Test LinkedList insert command works correctly."""
    from linked_list import LinkedList, Node
    input_ = [1, 2]
    ll_inst = LinkedList(input_)
    ll_inst.insert(3)
    assert ll_inst.tail.pointer.pointer.value == (Node(2, Node(1, Node(3,
                                                  None))).pointer.pointer.value
                                                  )


def test_linkedlist_insert_string():
    """Test LinkeList.insert for tail addition to Node list."""
    from linked_list import LinkedList
    input_ = [1, 2, 3]
    linked_list_instance = LinkedList(input_)
    linked_list_instance.insert("Nadia")
    assert linked_list_instance.tail.pointer.pointer.pointer.value == "Nadia"


def test_linkedlist_insert_empty():
    """Test LinkedList.insert from an empty list."""
    from linked_list import LinkedList
    input_ = []
    linked_list_instance = LinkedList(input_)
    linked_list_instance.insert('a')
    assert linked_list_instance.size() == 1


def test_linkedlist_pop():
    """Test LinkedList.pop for head removal."""
    from linked_list import LinkedList
    input_ = [1]
    linked_list_instance = LinkedList(input_)
    assert linked_list_instance.pop() == 1


def test_linkedlist_pop_empty():
    """Test LinkedList.pop from an empty list."""
    from linked_list import LinkedList
    input_ = []
    linked_list_instance = LinkedList(input_)
    with pytest.raises(IndexError):
        linked_list_instance.pop()


def test_linkedlist_size_long():
    """Test LinkedList.size for proper length return."""
    from linked_list import LinkedList
    input2_ = list(range(75))
    linked_list_instance2 = LinkedList(input2_)
    assert linked_list_instance2.size() == len(input2_)


def test_linkedlist_size_empty():
    """Test LinkedList.size for proper length return."""
    from linked_list import LinkedList
    input3_ = []
    linked_list_instance3 = LinkedList(input3_)
    assert linked_list_instance3.size() == len(input3_)


@pytest.fixture(scope='function')
def linked_list_instance():
    """Fixture for linkedlist search test."""
    from linked_list import LinkedList
    input_ = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    return LinkedList(input_)


def test_linkedlist_search_mid(linked_list_instance):
    """Test LinkedList.search for value match and return."""
    assert linked_list_instance.search("d").value == "d"


def test_linkedlist_search_head(linked_list_instance):
    """Test LinkedList.search for value match and return."""
    assert linked_list_instance.search("a").value == "a"


def test_linkedlist_search_missing(linked_list_instance):
    """Test LinkedList.search for value match and return."""
    assert linked_list_instance.search("norton is amazing") is None


def test_linkedlist_remove(linked_list_instance):
    """Test LinkedList.remove for proper mid-list Node removal."""
    from linked_list import Node
    linked_list_instance.remove(Node('y'))
    assert linked_list_instance.tail.pointer.value == 'x'


def test_linkedlist_remove_tail(linked_list_instance):
    """Test LinkedList.remove for proper first Node removal."""
    from linked_list import Node
    linked_list_instance.remove(Node('z'))
    assert linked_list_instance.tail.pointer.value == 'x'


def test_linkedlist_remove_head():
    """Test LinkedList.remove for proper last Node removal."""
    from linked_list import LinkedList, Node
    input_ = "a b c".split()
    linked_list_instance = LinkedList(input_)
    linked_list_instance.remove(Node('a'))
    assert linked_list_instance.tail.pointer.pointer is None


def test_linkedlist_display():
    """Test LinkedList.display for proper string formatting."""
    from linked_list import LinkedList
    input_ = "a b c".split()
    linked_list_instance = LinkedList(input_)
    assert linked_list_instance.display() == "('c', 'b', 'a')"
