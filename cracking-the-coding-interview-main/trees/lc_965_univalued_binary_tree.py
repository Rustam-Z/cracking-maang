"""
LeetCode: 965. Univalued Binary Tree, https://leetcode.com/problems/univalued-binary-tree/

Problem: Given a root of tree, if all values in the tree are the same.

Solution:
1. Take the value of the root.
2. Use the BFS algorith, iteratively, because when you encounter the node.val != root.val, return False

Time: O(m), m is the number of nodes in the tree traversed, till we encounter not equal value.
Space: O(h), where h is the height of the tree.
"""


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return None

        number = root.val

        queue = deque()
        queue.append(root)

        while queue:
            curr = queue.popleft()

            if curr.val != number:
                return False
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return True

