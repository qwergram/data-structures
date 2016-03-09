# -*- coding=utf-8 -*-
"""Test LinkedList for random inputs."""
import pytest


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


def test_linkedlist_insert():
    """Test LinkedList insert command works correctly."""
    from linked_list import LinkedList, Node
    input_ = [1, 2]
    linked_list_instance = LinkedList(input_)
    assert linked_list_instance.tail.value == Node(2, Node(1, None)).value


def test_linkedlist_insert_b():
    """Test LinkedList insert command works correctly."""
    from linked_list import LinkedList, Node
    input_ = [1, 2]
    ll_inst = LinkedList(input_)
    assert ll_inst.tail.pointer.value == Node(2, Node(1, None)).pointer.value


def test_linkedlist_insert_c():
    """Test LinkedList insert command works correctly."""
    from linked_list import LinkedList, Node
    input_ = [1, 2]
    ll_inst = LinkedList(input_)
    ll_inst.insert("a")
    assert ll_inst.tail.pointer.pointer.value == (Node(2, Node(1, Node("a",
                                                  None))).pointer.pointer.value
                                                  )


def test_linkedlist_constructor():
    """Test LinkedList contstructor for functionality."""
    from linked_list import LinkedList
    assert LinkedList.tail is None


def test_linkedlist_constructor_b():
    """Test LinkedList contstructor for functionality."""
    from linked_list import LinkedList, Node
    input_ = [1, 2]
    linked_list_instance = LinkedList(input_)
    assert isinstance(linked_list_instance.tail, Node)


def test_linkedlist_constructor_c():
    """Test LinkedList contstructor for functionality."""
    from linked_list import LinkedList, Node
    input_ = [1, 2]
    linked_list_instance = LinkedList(input_)
    assert linked_list_instance.tail.value == Node(2, Node(1, None)).value


def test_linkedlist_constructor_d():
    """Test LinkedList contstructor for functionality."""
    from linked_list import LinkedList, Node
    input_ = [1, 2]
    ll_inst = LinkedList(input_)
    assert ll_inst.tail.pointer.value == Node(2, Node(1, None)).pointer.value


def test_linkedlist_constructor_e():
    """Test LinkedList contstructor for functionality."""
    from linked_list import LinkedList
    input_ = [1, 2]
    linked_list_instance = LinkedList(input_)
    assert linked_list_instance.tail.pointer.pointer is None


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


def test_linkedlist_size_small():
    """Test LinkedList.size for proper length return."""
    from linked_list import LinkedList
    input_ = list(range(5))
    linked_list_instance = LinkedList(input_)
    assert linked_list_instance.size() == len(input_)


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


def test_linkedlist_search_mid():
    """Test LinkedList.search for value match and return."""
    from linked_list import LinkedList
    input_ = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    linked_list_instance = LinkedList(input_)
    assert linked_list_instance.search("d").value == "d"


def test_linkedlist_search_head():
    """Test LinkedList.search for value match and return."""
    from linked_list import LinkedList
    input_ = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    linked_list_instance = LinkedList(input_)
    assert linked_list_instance.search("a").value == "a"


def test_linkedlist_search_missing():
    """Test LinkedList.search for value match and return."""
    from linked_list import LinkedList
    input_ = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    linked_list_instance = LinkedList(input_)
    assert linked_list_instance.search("norton is amazing") is None


def test_linkedlist_remove():
    """Test LinkedList.remove for proper mid-list Node removal."""
    from linked_list import LinkedList, Node
    input_ = 'a b c'.split()
    linked_list_instance = LinkedList(input_)
    linked_list_instance.remove(Node('b'))
    assert linked_list_instance.size() == 2


def test_linkedlist_remove_b():
    """Test LinkedList.remove for proper mid-list Node removal."""
    from linked_list import LinkedList, Node
    input_ = 'a b c'.split()
    linked_list_instance = LinkedList(input_)
    linked_list_instance.remove(Node('b'))
    assert linked_list_instance.tail.value == Node('c', Node('a', None)).value


def test_linkedlist_remove_c():
    """Test LinkedList.remove for proper mid-list Node removal."""
    from linked_list import LinkedList, Node
    input_ = 'a b c'.split()
    linked_list_instance = LinkedList(input_)
    linked_list_instance.remove(Node('b'))
    assert linked_list_instance.tail.pointer.value == (Node('c', Node('a',
                                                       None)).pointer.value)


def test_linkedlist_remove_first():
    """Test LinkedList.remove for proper first Node removal."""
    from linked_list import LinkedList, Node
    input_ = 'a b c'.split()
    linked_list_instance = LinkedList(input_)
    linked_list_instance.remove(Node('a'))
    assert linked_list_instance.tail.value == Node('c', Node('b', None)).value


def test_linkedlist_remove_first_b():
    """Test LinkedList.remove for proper first Node removal."""
    from linked_list import LinkedList, Node
    input_ = 'a b c'.split()
    linked_list_instance = LinkedList(input_)
    linked_list_instance.remove(Node('a'))
    assert linked_list_instance.tail.pointer.value == (Node('c', Node('b',
                                                       None)).pointer.value)


def test_linkedlist_remove_first_c():
    """Test LinkedList.remove for proper first Node removal."""
    from linked_list import LinkedList, Node
    input_ = 'a b c'.split()
    linked_list_instance = LinkedList(input_)
    linked_list_instance.remove(Node('a'))
    assert linked_list_instance.tail.pointer.pointer is None


def test_linkedlist_remove_last():
    """Test LinkedList.remove for proper last Node removal."""
    from linked_list import LinkedList, Node
    input_ = 'a b c'.split()
    linked_list_instance = LinkedList(input_)
    linked_list_instance.remove(Node('c'))
    assert linked_list_instance.tail.value == Node('b', Node('a', None)).value


def test_linkedlist_remove_last_b():
    """Test LinkedList.remove for proper last Node removal."""
    from linked_list import LinkedList, Node
    input_ = 'a b c'.split()
    ll_inst = LinkedList(input_)
    ll_inst.remove(Node('c'))
    assert ll_inst.tail.pointer.value == (Node('b', Node('a', None)).pointer
                                          .value)


def test_linkedlist_remove_last_c():
    """Test LinkedList.remove for proper last Node removal."""
    from linked_list import LinkedList, Node
    input_ = 'a b c'.split()
    linked_list_instance = LinkedList(input_)
    linked_list_instance.remove(Node('c'))
    assert linked_list_instance.tail.pointer.pointer is None


def test_linkedlist_display():
    """Test LinkedList.display for proper string formatting."""
    from linked_list import LinkedList
    input_ = "a b c".split()
    linked_list_instance = LinkedList(input_)
    assert linked_list_instance.display() == "('c', 'b', 'a')"


def test_stack_push_tail():
    """Test Stack. push method."""
    from stack import Stack
    input_ = ['sad']
    stack_instance = Stack(input_)
    stack_instance.push('happy')
    assert stack_instance.tail.value == 'happy'


def test_stack_push_pointer():
    """Test Stack. push method."""
    from stack import Stack
    input_ = ['sad']
    stack_instance = Stack(input_)
    stack_instance.push('happy')
    assert stack_instance.tail.pointer.value == 'sad'


def test_stack_pop():
    """Test Stack.pop method."""
    from stack import Stack
    input_ = [1]
    stack_instance = Stack(input_)
    assert stack_instance.pop() == 1
