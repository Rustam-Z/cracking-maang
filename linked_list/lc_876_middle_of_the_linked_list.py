"""
LeetCode: https://leetcode.com/problems/middle-of-the-linked-list/

Problem: 876. Middle of the Linked List

Input: Linked list head
Output: Middle node of LL

SOLUTION 1:
    - Make array out of LL
    - Then find middle element
    - Time: O(n)
    - Space: O(n)
SOLUTION 2:
    - Slow and fast pointer
    - Fast moves two time before than slow
    - Time: O(n)
    - Space: O(1)
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow, fast = head, head
        try:
            while fast.next:
                slow = slow.next
                fast = fast.next.next
        except:
            pass

        return slow

    def middle_node_better_solution(self, head):
        if not head:
            return None

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        if fast.next:
            return slow.next
        else:
            return slow
