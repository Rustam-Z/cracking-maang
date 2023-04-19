"""
LeetCode: https://leetcode.com/problems/add-two-numbers-ii/

Problem: 1200 + 209 = 1409

Time: O(n + m)
Space: O(1)
"""

from linked_list import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def convertToNumber(head):
            num = 0
            while head is not None:
                num = num*10 + head.val
                head = head.next
            return num
        
        head = None
        sum = convertToNumber(l1) + convertToNumber(l2);
        
        while sum > 0:
            r = sum % 10
            node = ListNode(r)
            if (head is None):
                head = node
            else:
                node.next = head
                head = node
            
            sum = sum // 10
        
        if (head is None):
            head = ListNode(0)
        
        return head
    
    
