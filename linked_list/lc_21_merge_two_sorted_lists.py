"""
LeetCode: https://leetcode.com/problems/merge-two-sorted-lists/

Problem: Merge Two Sorted Lists

Input: Two heads of linked lists
Output: Merged list

SOLUTION 1:
    - Convert the LL to array
    - Combine both arrays
    - Sort the resultant array
    - Create another LL
    - Time comp: O(nlogn) where n is len of longer LL
    - Space comp: O(n)
SOLUTION 2:
    - Iterate over both lists at the same time
    - Create a dummy node, and insert one by one
    - After loop finish, insert the tail that left
    - Time: O(n)
    - Space: O(1)
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        dummy = ListNode()
        curr = dummy

        while list1 and list2:

            if list1.val >= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return dummy.next
