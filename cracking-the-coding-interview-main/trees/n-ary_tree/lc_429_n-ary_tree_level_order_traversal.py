"""
429. N-ary Tree Level Order Traversal
https://leetcode.com/problems/n-ary-tree-level-order-traversal/

Problem: given the N-ary tree, return array which is level order traversal.

Solution:
    - Implement BFS algorithm.
    - Same as binary tree, but instead of checking node.left and node.right we do queue.extend(node.children).
"""
from collections import deque


# O(N) time | O(N) space
def levelOrder(self, root):
    result = []

    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        values = []
        for i in range(len(queue)):
            node = queue.popleft()
            values.append(node.val)

            queue.extend(node.children)

        result.append(values)

    return result
