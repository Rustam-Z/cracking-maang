"""
Leetcode: https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/

Problem: given the middle node (it is not the middle of linked list), we need to delete that node.

Solution:
! If the node to be deleted is the last we can't handle it
1. We have access to next pointer, just copy values
2. Check to node.next should not be None (if not return False)
3. Then change pointer of node.next to node.next.next

Time: O(1)
Space: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_middle_node(node: ListNode) -> bool:
    if node is None or node.next is None:
        return False
    
    node.val = node.next.val 
    node.next = node.next.next 
    return True 
