
def test_LinkedList_constructor():
    from linked_list import LinkedList, Node
    input_ = [1, 2]

    linked_list_instance = LinkedList(input_)

    assert LinkedList.tail is None
    assert isinstance(linked_list_instance.tail, Node)
    assert linked_list_instance.tail.value == Node(2, Node(1, None)).value
    assert linked_list_instance.tail.pointer.value == Node(2, Node(1, None)).pointer.value
    assert linked_list_instance.tail.pointer.pointer == None


def test_LinkedList_pop():
    from linked_list import LinkedList, Node
    input_ = [1,2,3]

    linked_list_instance = LinkedList(input_)

    assert linked_list_instance.tail.value == Node(3, Node(2, Node(1, None))).value


def test_LinkedList_count():
    from linked_list import LinkedList, Node
    input_ = list(range(5))
    input2_ = list(range(75))

    linked_list_instance = LinkedList(input_)
    linked_list_instance2 = LinkedList(input2_)


    assert linked_list_instance.size() == len(input_)
    assert linked_list_instance2.size() == len(input2_)


def test_LinkedList_search():
    from linked_list import LinkedList, Node

    input_ = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()

    linked_list_instance = LinkedList(input_)

    assert linked_list_instance.search("d").value == "d"
    assert linked_list_instance.search("a").value == "a"
    assert linked_list_instance.search("norton is amazing") is None
