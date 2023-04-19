"""
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
1290. Convert Binary Number in a Linked List to Integer

NOTE! See how to convert binary to decimal
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        def bin_to_dec(num):
            counter = 0
            sum_ = 0
            while num > 0:
                r = num % 10
                sum_ = sum_ + (2 ** counter) * r
                num //= 10
                counter += 1
            print(sum_)
            return sum_

        binary_num = 0

        curr = head
        while curr is not None:
            binary_num = binary_num * 10 + curr.val
            curr = curr.next
        print(binary_num)

        return bin_to_dec(binary_num)
