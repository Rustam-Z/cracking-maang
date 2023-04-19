"""
Leetcode: https://leetcode.com/problems/add-two-numbers/
          https://leetcode.com/problems/add-two-numbers-ii/

Problem: given two lists in reversed order, sum them, and return digit of sum also in reversed order.

Solution:
1. Use dummy, create a reference to dummy
2. Use carry 
3. Not to check if the l1 or l2 has some nodes after iterating through while,
we need to use OR and assign node value to 0 if it finished
4. sum = x + y + carry, it could be maximum 19
5. carry_ = sum_ // 10, for example 19 // 10 == 1
6. Create a new node with value sum_ % 10, 19 % 10 == 9
7. Add the new node to the head of the list
8. Check for l1 and l2 is not None
9. After finishing, check one more time if carry is 1, then add a new node

Time: O(n + m)
Space: O(1)
"""

from linked_list import ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        result = dummy
        carry = 0
        
        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            
            sum_ = x + y + carry
            carry = sum_ // 10

            result.next = ListNode(sum_ % 10)
            result = result.next
            
            if l1 is not None:            
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        if carry:
            node = ListNode(1)
            result.next = node

        return dummy.next
