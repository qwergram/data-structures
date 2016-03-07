
def test_LinkedList_constructor():
    from linked_list import LinkedList, Node
    input_ = [1, 2]

    ListInstance = LinkedList(input_)

    assert LinkedList.tail is None
    assert ListInstance.tail.value == Node(2, Node(1)).value
    assert ListInstance.tail.pointer == Node(2, Node(1)).pointer
