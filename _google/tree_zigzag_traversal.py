"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Input: root = [3,9,20,null,null,15,7]
     3
    / \
   9   20
      /  \
    15    7
Output: [[3],[20,9],[15,7]]

Solution:
    - BFS with a queue
    - Use a flag to indicate whether to reverse the level traversal
    - Time complexity: O(n)
    - Space complexity: O(n)
"""
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    traversal = []

    if not root:
        return traversal

    queue = deque()
    is_from_left_to_right = True
    queue.append(root)

    while queue:
        level_traversal = []

        for _ in range(len(queue)):
            node = queue.popleft()
            level_traversal.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if is_from_left_to_right:
            traversal.append(level_traversal)
        else:
            traversal.append(level_traversal[::-1])

        is_from_left_to_right = not is_from_left_to_right

    return traversal
