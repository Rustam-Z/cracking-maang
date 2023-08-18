"""
Problem:
    Given the head of a linked list and a value x,
    partition it such that all nodes less than x come before nodes greater than or equal to x.

Questions and Clarifications:
    - Should we create a new linked list or modify the existing one? BETTER: to create new
    - Do we need to preserve the original order of the nodes?
    - Will we have negative values? Or duplicates?
    - Can all values be less than x? Or greater than or equal to x? Or all value be equal to x?
"""
from collections import deque


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def solution1_brute_force(head: ListNode, pivot: int) -> ListNode:
    """
    Algorithm:
        - Convert linked list to array
        - Partition the array, place numbers less than pivot to the left, and others to right
        - Create new linked list

    Time complexity: O(n)
    Space complexity: O(n)
    """
    # STEP 1: Convert linked list to array
    array = []
    curr = head
    while curr:
        array.append(curr.value)
        curr = curr.next

    # STEP 2: Partition the array, place numbers less than pivot to the left, and others to right
    array = _partition_array(array, pivot)

    # STEP 3: Create new linked list
    new_head = ListNode(array[0])
    curr = new_head
    for num in array[1:]:
        curr.next = ListNode(num)
        curr = curr.next

    return new_head


def solution2_two_linked_lists(head: ListNode, pivot: int) -> ListNode:
    """
    Algorithm:
        - Create two linked lists: one for numbers less than pivot, and one for others
        - Traverse the original linked list, and append each node to the corresponding linked list
        - Merge the two linked lists

    Time complexity: O(n)
    Space complexity: O(n)
    """
    # STEP 1: Create two linked lists: one for numbers less than pivot, and one for others
    less_than_pivot_head = ListNode()
    greater_than_or_equal_to_pivot_head = ListNode()
    less_than_pivot_curr = less_than_pivot_head
    greater_than_or_equal_to_pivot_curr = greater_than_or_equal_to_pivot_head

    # STEP 2: Traverse the original linked list, and append each node to the corresponding linked list
    curr = head
    while curr:
        if curr.value < pivot:
            less_than_pivot_curr.next = curr
            less_than_pivot_curr = less_than_pivot_curr.next
        else:
            greater_than_or_equal_to_pivot_curr.next = curr
            greater_than_or_equal_to_pivot_curr = greater_than_or_equal_to_pivot_curr.next

        curr = curr.next

    # STEP 3: Merge the two linked lists
    less_than_pivot_curr.next = greater_than_or_equal_to_pivot_head.next
    greater_than_or_equal_to_pivot_curr.next = None

    return less_than_pivot_head.next


def _partition_array(array: list, pivot: int) -> list:
    # STEP 2: Partition the array, place numbers less than pivot to the left, and others to right
    new_array = deque()
    for num in array:
        if num < pivot:
            new_array.appendleft(num)
        else:
            new_array.append(num)

    return list(new_array)
