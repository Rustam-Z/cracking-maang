"""
LeetCode: https://leetcode.com/problems/linked-list-cycle-ii/

Problem: 142. Linked List Cycle II

Input: Linked list head
Output: Linked list node where the cycle begins

SOLUTION 1:
    - Slow and fast pointers
    -
    - Time: O(n)
    - Space: O(1)
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                break
        else:
            return None

        curr = head
        while curr != slow:
            slow = slow.next
            curr = curr.next
        return curr

