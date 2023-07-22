"""430. Flatten a Multilevel Doubly Linked List
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

Problem:
    Given the linked list, and the nodes may have children. And you have to flatten the linked list.

Questions
    - What values should the children have after we change them?
    - How many levels deep we can go?

Solution:
    - use the stack data structure?
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        dummy = Node(0)
        curr, stack = dummy, [head]

        while stack:
            tmp = stack.pop()

            if tmp.next:
                stack.append(tmp.next)
            if tmp.child:
                stack.append(tmp.child)

            curr.next = tmp
            tmp.prev = curr
            tmp.child = None

            curr = tmp

        dummy.next.prev = None

        return dummy.next
