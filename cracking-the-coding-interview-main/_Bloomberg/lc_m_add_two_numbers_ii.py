"""445. Add Two Numbers II
https://leetcode.com/problems/add-two-numbers-ii/

Problem: given two linked lists. Find the sum of the numbers. And return another linked iist.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.get_val(l1)
        num2 = self.get_val(l2)
        total = self.str2int(num1) + self.str2int(num2)
        print(total)

        dummy = ListNode()
        curr = dummy

        for char in str(total):
            node = ListNode(char)
            curr.next = node
            curr = curr.next
        return dummy.next

    def get_val(self, node) -> str:
        num = ''
        while node:
            num = "".join([num, str(node.val)])
            node = node.next
        return num

    def str2int(self, num: str) -> int:
        int_num = 0
        for char in num:
            int_num = int_num * 10 + ord(char) - ord('0')
        return int_num


class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rev1 = l1
        rev2 = l2
        rev1Val = 0
        rev2Val = 0
        while rev1 or rev2:
            if rev1:
                rev1Val = rev1Val * 10 + int(rev1.val)
                rev1 = rev1.next

            if rev2:
                rev2Val = rev2Val * 10 + int(rev2.val)
                rev2 = rev2.next

        total = rev1Val + rev2Val

        cur = None
        if total == 0:
            return ListNode(0)

        while total > 0:
            remain = total % 10
            total //= 10
            n = ListNode(remain)
            n.next = cur
            cur = n

        return cur
