"""
19. Remove Nth Node From End of List

Problem: Given the head of a linked list, remove the nth node from the end of the list and return its head.

Solution 2:
1. First need to change the n to count from the beginning
2. need to traverse through the LL, with count
3. Use two pointers prev, curr (prev = curr, curr = curr.next)

Solution 1:
1. Go till the fast n times
2. Check if fast is None return head.next, it happens when fast is the last element, or the only element
3. Then check till fast.next goes to the end
4. Delete the node with slow.next = slow.next.next

General idea, placing the fast to N, then starting iterating.

Time: O(n)
Space: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Better solution
        """
        if head is None:
            return None
        
        slow = head
        fast = head

        for i in range(n):
            fast = fast.next
            
        if fast is None:
            return head.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next                
        return head

    def checkLenghtToRemoveNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 0. First need to change the n to count from the beginning
        # 1. need to traverse through the LL, with count
        # 2. prev, curr

        curr = head
        count_length = 0

        while curr is not None:
            curr = curr.next
            count_length += 1

        target = count_length - n + 1  # Target index from the beginning

        if target == 1:
            return head.next

        prev_node = head
        curr = head
        count_length = 0

        while curr is not None:
            count_length += 1

            if count_length == target:
                prev_node.next = curr.next
            prev_node = curr
            curr = curr.next

        return head
