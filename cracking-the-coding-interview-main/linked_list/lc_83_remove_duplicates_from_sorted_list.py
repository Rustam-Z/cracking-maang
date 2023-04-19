"""
83. Remove Duplicates from Sorted List

Problem: Given a sorted linked list, delete all duplicates such that each element appear only once.

Solution:
0. Check for head is None
1. Create two pointers prev = head, and curr = head.next
2. Check if their values are the same, cheange prev.next to curr.next
3. Else, just move prev = prev.next
4. Always change curr = curr.next

Time: O(n)
Space: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(self, head: ListNode) -> ListNode:
    if head is None:
        return None
    
    prev = head
    curr = head.next
    
    while prev.next is not None:
        if curr.val == prev.val:
            prev.next = curr.next
        else:
            prev = prev.next
        curr = curr.next
            
    return head
