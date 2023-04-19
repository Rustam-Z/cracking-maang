"""
A linked list is a data structure that represents a sequence of nodes. 
In a singly linked list, each node points to the next node in the linked list. 
A doubly linked list gives each node pointers to both the next node and the previous node.

LL doesn't provide constant access time to the node at a given index. You need to iterate K times to get to the node
at index K. But in LL you can add / delete at the beginning / end of list in O(1).
"""
from typing import Any


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList:
    size = 0

    def __init__(self):
        self.head = None

    def get(self, index: int) -> Any | None:
        if index < 0 or index >= self.size:
            return None

        if self.head is None:
            return None

        curr = self.head
        for i in range(index):
            curr = curr.next

        return curr.val

    def add_at_head(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def add_at_tail(self, val: int) -> None:
        curr = self.head

        if curr is None:
            self.head = ListNode(val)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = ListNode(val)

        self.size += 1

    def add_at_index(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return None

        if index == 0:
            self.add_at_head(val)
        else:
            curr = self.head
            # taking the partition till "index"
            for i in range(index - 1):
                curr = curr.next

            node = ListNode(val)
            node.next = curr.next
            curr.next = node

            self.size += 1

    def delete_at_head(self) -> None:
        if self.head is None:
            return None
        self.head = self.head.next
        self.size -= 1

    def delete_at_tail(self) -> None:
        if self.head is None:
            return None

        prev = None
        curr = self.head
        while curr.next is not None:
            prev = curr
            curr = curr.next
        prev.next = None
        self.size -= 1

    def delete_at_index(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return None

        if index == 0:
            self.delete_at_head()
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next

            curr.next = curr.next.next
            self.size -= 1

    def __repr__(self):
        nodes = []

        curr = self.head
        while curr is not None:
            nodes.append(str(curr.val))
            curr = curr.next

        return "->".join(nodes)


if __name__ == "__main__":
    obj = LinkedList()

    obj.add_at_head(1)
    obj.add_at_head(2)
    obj.add_at_head(3)
    print("Linked list, len():", obj, obj.size)
    print("Object in Nth position:", obj.get(2))
    obj.add_at_tail(4)
    print(obj)
    obj.add_at_index(1, 56)
    print(obj)
    obj.delete_at_head()
    print(obj)
    obj.add_at_index(4, 25)
    print(obj)
    obj.delete_at_index(0)
    print(obj)
    obj.delete_at_tail()
    print(obj)
