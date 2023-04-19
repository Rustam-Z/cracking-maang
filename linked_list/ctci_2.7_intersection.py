""" 
LeetCode: https://leetcode.com/problems/intersection-of-two-linked-lists/

Problem: Given two singly linked lists, determine if the two lists intersect. Return the intersecting node.
Not by value, but by reference. If the nodes have similar values, they don't have the same address in memory.

Solution:
0. Compare by reference, not by value. Intersection means, they have the same ending. 
1. Find the max and min lists by length.
2. FInd the diff.
3. Move the longer node by diff > 0. Intersection ending is the same for LL. Just beginning is different, we need to find it by moving longer.
4. Check if heads of both long and short lists are the same, till they are not the same.
5. Even if lists don't have intersection, return head longer, because till that moment it will reach 0. As head.next = 0 in the end. 

Time: O(max(headA, headB))
Space: O(1)
"""
from linked_list import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = self.findLen(headA), self.findLen(headB)
        diff = lenA - lenB
        headL = headA if diff >= 0 else headB
        headS = headB if headL is headA else headA
        diff = abs(diff)
        
        while diff > 0:
            headL = headL.next
            diff -= 1
     
        while headL != headS:
            headL = headL.next
            headS = headS.next
            
        return headL
        
    def findLen(self, head):
        length = 0
    
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        return length
