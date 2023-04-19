""" 
LeetCode: https://leetcode.com/problems/palindrome-linked-list/

Problem: check is the linked list is palindrome.

Solution:
0. Use stack, go till middle by pushing, and pop another middle.
1. Use fast and slow pointers. Fast pointer moves 2 steps at a time, slow pointer moves 1 step at a time.
2. While fast reaches the end, the slow will stand in middle.
3. Check for even and odd length of LL. If odd fast will be in last element (not None), move slow to one (slow = slow.next).
4. Pop from stack compare with slow.val. Slow ptr is in middle.

Time: O(n)
Space: O(n)
"""

from linked_list import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
           return None
        if head.next is None:
            return True
        
        stack = []
        
        fast, slow = head, head
        while fast and fast.next:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next
            
        if fast is not None:
            slow = slow.next
            
        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next
            
        return True


class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return None
        
        # Let's make a O(1) space algorithm
        
        # 1. find middle (slow, fast pointers)
        # 2. reverse the second half
        # 3. check palindrome
        
        slow, fast = head, head
        
        # Find middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # Reverse the second half, 1221 -> 1212
        prev = None
        while slow:
            tmp = slow.next
            
            slow.next = prev
            prev = slow
            slow = tmp
            
        # Check the palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True
        