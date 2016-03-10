
class Node(object):

    def __init__(self, value, next, prev):

        # Require the user to explicitly state the pointers
        # as per zen of python line 2 (python -m this)
        self.value = value
        self.next = next  # In other words: pointer towards the tail
        self.prev = prev  # In other words: previous towards the head


class DoublyLinkedList(object):

    # The reason why this was so frustratingly hard, was because we weren't
    # utilizing this self.head = None statement. If we keep track of the head
    # and tail, this problem becomes easier.

    # It was quite difficult trying to solve this problem, so I got some help
    # with my logic from the following site:
    # http://ls.pwd.io/2014/08/singly-and-doubly-linked-lists-in-python/
    # It also contains some articles about singly linked lists.

    head = None
    tail = None

    def __init__(self, values):
        """Accept a list of values and generate a chain of Nodes using those values"""
        # if the value is a list, iterate through them and insert them to the list
        if isinstance(values, list):
            for value in values:
                # I imagined this to be like blocks on a conveyor belt
                # It falls off into a pit and the last one in is the first one
                # out, so we use append.
                self.append(value)
        else:
            # Don't deal with anything else, and make it clear that we don't
            # want to.
            raise TypeError("Please package your item into a list!")

    def append(self, value):
        """Append a value to the tail of the linked list"""
        # Create a new node object with null pointers (pun not intended)
        new_node = Node(value, None, None)
        if self.head is None:  # If head or tail don't have values, it's safe to assume that the other doesn't either so check one...
            # If there isn't a value already, it means that neither don't.
            # So set both to the new_node. We're done.
            self.head = self.tail = new_node
        else:
            # However, if there is already a value there, we need to insert it to the head of the list
            # So set the previous of the new_node to the existing tail to extend the tail
            new_node.prev = self.tail
            # a syntatic sugar, but set the next pointer to a null value (which we already did)
            new_node.next = None
            # set the previous item's next pointer to point the new_node
            self.tail.next = new_node
            # and then set the actual tail to the new_node
            self.tail = new_node

    def insert(self, value):
        """Insert a value to the head of the linked list"""
        # Same exact thing as the append method, but the logic is backwards, so to speak...
        # create our new node like usual with null pointers
        new_node = Node(value, None, None)
        if self.head is None:  # If head or tail don't have values, it's safe to assume that the other doesn't either so check one...
            # If there isn't a value already, it means that neither don't.
            # So set both to the new_node. We're done.
            self.head = self.tail = new_node
        else:
            # However, if there is already a value there, we need to insert it to the head of the list
            # So set the previous of the new_node to the existing tail to extend the tail
            new_node.next = self.head
            # a syntatic sugar, but set the next pointer to a null value (which we already did)
            new_node.prev = None
            # set the previous item's next pointer to point the new_node
            self.head.prev = new_node
            # and then set the actual tail to the new_node
            self.head = new_node

    def pop(self):
        """Remove the head of the chain and return the Node"""
        # Pop will look at the head of the chain and remove it and delete the
        # Node.prev pointer and set that to None
        if self.head is None:
            # the head or tail is none, we can't pop so raise an exception
            raise IndexError("Cannot pop an empty list!")
        else:
            # however if there is something at head, we can continue with our operation
            # save the current head as old_head so we can return the node
            old_head = self.head
            # The next head will be the next item stepping towards the tail, so .next
            # set that as the new var
            new_head = self.head.next
            # since we're deleting the old head, remove all pointers that point to it
            new_head.prev = None
            # set the object head to the new_head
            self.head = new_head
            # Reset the pointers so the old_head can be garbage collected if need be
            # If you move this above self.head = new_head, your pointers will collide
            # and throw errors. Keep this below the new pointer assignment.
            old_head.next = None
            old_head.prev = None
            # Return the node that was popped without the pointers
            return old_head

    def shift(self):
        """Remove the tail of the chain and return the Node"""
        # shift is basically pop, but it's opposite or backwards, so to speak.
        # Let's do our check again, make sure that there are values to do deal with
        if self.head is None:
            # and if there's nothing to shift, raise the exception!
            raise IndexError("Cannot shift an empty list!")
        else:
            # Now comes our code. Theoretically, we could move this all outside of an else block
            # So let's set an old_tail so we can return it later
            old_tail = self.tail
            # The next tail will be the previous item stepping towards the head, so .prev
            # of the current tail is the new tail
            new_tail = self.tail.prev
            # since we're deleting the old tail, remove all pointers that point to it
            new_tail.next = None
            # set the object tail to the new tail
            self.tail = new_tail
            # Now reset the pointers in the old tail for garbage collecting
            old_tail.next = None
            old_tail.prev = None
            # Now return the old_tail
            return old_tail

    def remove(self, value):
        """Remove the specified item from the node chain and rebind the Nodes agian"""
        # before we do anything related to remove, check that if it's at the tail or head of the chain
        # Before checking the .value, make sure that tail isn't none as well
        if self.tail is not None and self.tail.value == value:
            # if the value happens to be the tail, then we can just call shift
            self.shift()
        elif self.head is not None and self.head.value == value:
            # if the value happens to be the head, then we can just call pop
            self.pop()
        else:
            # set a cursor to our current head
            current_node = self.head
            # set a keep the old cursor in memory, but since there isn't a previous
            # cursor now, set it to none
            previous_node = None
            while current_node is not None:  # While the current Node is indeed a Node object...
                if current_node.value == value:  # if the node we're looking at currently holds the value...
                    # if the previous_node is None, that means the first item in the chain starting
                    # from the head is the value we want to remove
                    if previous_node is not None:  # if the item isn't the first one in the chain...
                        # set the previous_node.next to the current_node.next
                        previous_node.next = current_node.next
                        # set the .prev of the next to the previous node
                        previous_node.next.prev = previous_node
                    else:
                        # if the item is the first link in the chain
                        # just remove it entirely without worrying about pointers
                        self.head = current_node.next
                    # since we only want to remove one instance, break from the loop
                    break
                # move the cursor one step closer to the tail
                previous_node = current_node
                current_node = current_node.next
            else:
                # if the loop completes without a break, that means the item was not
                # found. In that case we'll raise a ValueError
                raise ValueError("Item was not found in list!")
