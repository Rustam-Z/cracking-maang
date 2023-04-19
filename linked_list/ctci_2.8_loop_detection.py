"""
LeetCode: https://leetcode.com/problems/linked-list-cycle-ii/

Problem: Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

Solution:
1. Use fast and slow pointers. Fast pointer moves 2 steps at a time, slow pointer moves 1 step at a time.
2. Go till fast will not meet slow. If they meet break loop. If they don't meet, it means, there is no cycle and fast will be None, then return None.
3. Now you need to find the start of cycle. Because they might meet in the middle of the circle.
4. Use head and slow. While loop till head != slow. Move them by one. If they meet, it means, they are in the same node. Return one of them.

Time: O()
Space: O(1)
"""

from linked_list import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
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
