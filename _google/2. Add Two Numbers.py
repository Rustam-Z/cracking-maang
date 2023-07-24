"""
https://leetcode.com/problems/add-two-numbers/

Problem: Give 2 linked lists with integers, sum them, and return the result as a linked list.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]

Questions and constraints:
    - Can we have negative integers?
    - Can we have 0 as a value?
    - Can we have empty linked list?
    - Can we have different length of linked lists?

Solution:
    1. Create a dummy node to keep track of the head of the linked list.
    2. Create a carry variable to keep track of the carry.
    3. Iterate through both linked lists and sum the values.
    4. If the sum is greater than 10, then we have a carry.
    5. Create a new node with the sum % 10.
    6. Move the current node to the next node.
    7. Return the dummy node's next node.

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Solution 1: Create integers, sum two integers, create linked list.
        Solution 2: Use LL to sum two integers.
        """

        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum_ = v1 + v2 + carry
            carry, node_value = divmod(sum_, 10)
            new_node = ListNode(node_value)
            curr.next = new_node

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # if you don't want carry, then use while l1 or l2 or carry:
        if carry > 0:
            new_node = ListNode(carry)
            curr.next = new_node

        return dummy.next

    def addTwoNumbersBruteForce(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_val(list_):
            num = ''
            while list_:
                num += str(list_.val)
                list_ = list_.next

            return int(num[::-1])

        num1 = get_val(l1)
        num2 = get_val(l2)
        sum_ = num1 + num2
        dummy = curr = ListNode(next=None)

        for i in str(sum_)[::-1]:
            node = ListNode(val=int(i))
            curr.next = node
            curr = curr.next

        return dummy.next
