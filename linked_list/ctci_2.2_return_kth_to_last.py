"""
Algorithm which returns the kth last element of a singly linked list.

Solution:
1. Slow and fast pointers
2. Put fast in k initally
3. Move both pointers by 1 till fast.next is None
4. Constaint: k should be larger than len(LinkedList), and k should be negative

Time: O(n)
Space: O(1)
"""


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def return_kth_to_last(head: ListNode, k: int) -> ListNode:
    slow = head
    fast = head

    for i in range(k):
        fast = fast.next
    print("Fast, slow:", fast.val, slow.val)

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    return slow.val


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    kth_to_last = return_kth_to_last(node1, 2)
    print(kth_to_last)
