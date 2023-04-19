"""
86. Partition List

Input: head (ListNode), x (int)
Output: ListNode

Problem: place nodes with values small x to left side, bigger values to right side

Solution:
1. Create two lists left and right, and dummies which are the beginning point of each newly created lists
2. If value is smaller add node to left else to right
3. Concatenate them left.next = dummy_right.next

Time: O(n)
Space: O(1)
"""

from linked_list import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None:
            return None
    
        if head.next is None:
            return head
        
        left = ListNode(0)
        dummy_left = left
        
        right = ListNode(0)
        dummy_right = right  
        
        curr = head
        while curr is not None:
            tmp = ListNode(curr.val)
            if tmp.val < x:
                left.next = tmp
                left = left.next
            else:
                right.next = tmp
                right = right.next
            
            curr = curr.next
            
        print(dummy_left.next, "\n", dummy_right.next)
        
        # Concatenate two lists
        left.next = dummy_right.next
        return dummy_left.next
        