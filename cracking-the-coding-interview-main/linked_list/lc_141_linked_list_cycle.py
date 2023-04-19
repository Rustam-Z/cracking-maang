"""
LeetCode: https://leetcode.com/problems/linked-list-cycle/

Problem: 141. Linked List Cycle

Input: Linked list head
Output: True or False

SOLUTION 1:
    - Slow and fast pointers, Floyd's Cycle Detection
    - Traverse linked list using two pointers.
    = Move one pointer(slow_p) by one and another pointer(fast_p) by two.
    - If these pointers meet at the same node then there is a loop. If pointers do not meet then linked list doesn’t have a loop.
    - Time: O(n)
    - Space: O(1)
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow, fast = head, head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False

    def has_cycle_solution2(self, head):
        slow, fast = head, head  # slow -> 1, fast -> 2

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
