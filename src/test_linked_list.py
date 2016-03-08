# -*- coding=utf-8 -*-
"""Test LinkedList for random inputs"""


def test_LinkedList_

def test_LinkedList_insert():
    """Test LinkedList insert command works correctly"""
    from linked_list import LinkedList, Node
    input_ = [1, 2]
    linked_list_instance = LinkedList(input_)

    # Assert that the LinkedList is initializing properly

    assert linked_list_instance.tail == Node(2, Node(1, None)).value
    assert linked_list_instance.tail.pointer.value == Node(2, Node(1, None)).pointer.value

    linked_list_instance.insert("a")

    assert linked_list_instance.tail.pointer.pointer.value == Node(2, Node(1, Node("a", None))).pointer.pointer.value


def test_LinkedList_constructor():
    """Test LinkedList contstructor for functionality"""
    from linked_list import LinkedList, Node
    input_ = [1, 2]
    linked_list_instance = LinkedList(input_)
    assert LinkedList.tail is None
    assert isinstance(linked_list_instance.tail, Node)
    assert linked_list_instance.tail.value == Node(2, Node(1, None)).value
    assert linked_list_instance.tail.pointer.value == Node(2, Node(1, None)).pointer.value
    assert linked_list_instance.tail.pointer.pointer is None


def test_LinkedList_pop():  # This never actually tests "pop"
    """Test LinkedList.pop for head removal"""
    from linked_list import LinkedList, Node
    input_ = [1, 2, 3]
    linked_list_instance = LinkedList(input_)
    assert linked_list_instance.tail.value == Node(3, Node(2, Node(1, None))).value


def test_LinkedList_size():
    """Test LinkedList.size for proper length return"""
    from linked_list import LinkedList
    input_ = list(range(5))
    input2_ = list(range(75))
    linked_list_instance = LinkedList(input_)
    linked_list_instance2 = LinkedList(input2_)
    assert linked_list_instance.size() == len(input_)
    assert linked_list_instance2.size() == len(input2_)


def test_LinkedList_search():
    """Test LinkedList.search for value match and return"""
    from linked_list import LinkedList
    input_ = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    linked_list_instance = LinkedList(input_)
    assert linked_list_instance.search("d").value == "d"
    assert linked_list_instance.search("a").value == "a"
    assert linked_list_instance.search("norton is amazing") is None


def test_LinkedList_remove():
    """Test LinkedList.remove for proper mid-list Node removal"""
    from linked_list import LinkedList, Node
    input_ = 'a b c'.split()
    linked_list_instance = LinkedList(input_)
    linked_list_instance.remove(Node('b'))
    assert linked_list_instance.tail.value == Node('c', Node('a', None)).value
    assert linked_list_instance.tail.pointer.value == Node('c', Node('a', None)).pointer.value


def test_LinkedList_remove_first():
    """Test LinkedList.remove for proper first Node removal"""
    from linked_list import LinkedList, Node
    input_ = 'a b c'.split()
    linked_list_instance = LinkedList(input_)
    linked_list_instance.remove('a')
    assert linked_list_instance.tail.value == Node('c', Node('b', None)).value
    assert linked_list_instance.tail.pointer.value == Node('c', Node('b', None)).pointer.value
    assert linked_list_instance.tail.pointer.pointer is None


def test_LinkedList_remove_last():
    """Test LinkedList.remove for proper last Node removal"""
    from linked_list import LinkedList, Node
    input_ = 'a b c'.split()
    linked_list_instance = LinkedList(input_)
    linked_list_instance.remove('c')
    assert linked_list_instance.tail.value == Node('b', Node('a', None)).value
    assert linked_list_instance.tail.pointer.value == Node('b', Node('a', None)).pointer.value
    assert linked_list_instance.tail.pointer.pointer is None


def test_LinkedList_display():
    """Test LinkedList.dispaly for proper string formatting"""
    from linked_list import LinkedList
    input_ = "a b c".split()
    linked_list_instance = LinkedList(input_)
    assert linked_list_instance.display() == "('c', 'b', 'a')"
