"""
LeetCode:

Problem: Given the tree and target, return the closest node value to target value.

SOLUTION 1:
    - DFS inorder (the result will be sorted array)
    - Then find the closest using binary search
    - Time: O(n)
    - Space: O(n)

SOLUTION 2:
    - Use the property of BST
    - Move to right subtree if target is bigger than node's value
    - If bigger move to left subtree
    - Update the value of "closest" variable
    - Trick: If diff is 0 then stop
    - TIme: O(logN), worst will be O(n) when we don't have a tree
    - Space: O(1), for iterative
"""


from typing import Any


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


# My solution
# Average: O(logN) time | O(logN) space
# Worst: O(N) time | O(N) space
def find_closest_value_iterative(root: TreeNode, target: int) -> Any | None:
    if not root:
        return None

    closest = root.val
    curr = root

    while curr:
        if abs(target - closest) > abs(target - curr.val):
            closest = curr.val

        if target > curr.val:
            curr = curr.right
        elif target < curr.val:
            curr = curr.left
        else:
            break  # The target == curr.val, and diff is 0

    return closest


# AlgoExpert solution
# Average: O(logN) time | O(1) space
# Worst: O(N) time | O(1) space
def find_closest_recursive(root, target):
    def helper(root, target, closest):
        if root is None:
            return closest

        if abs(target - closest) > abs(target - root.val):
            closest = root.val

        if target > root.val:
            return helper(root.right, target, closest)
        elif target < root.val:
            return helper(root.left, target, closest)
        else:
            return closest

    return helper(root, target, float("inf"))



