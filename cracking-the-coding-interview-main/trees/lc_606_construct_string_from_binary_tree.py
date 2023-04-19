"""
LeetCode: 606. Construct String from Binary Tree
https://leetcode.com/problems/construct-string-from-binary-tree/

Problem: Given tbe tree of the node,

Solution:
1. Use the DFS

Time: O(n)
Space: O(h), the height of the tree
"""


class Solution:
    def __init__(self):
        self.traversals = []

    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(root):
            if not root:
                return ''
            else:
                l = dfs(root.left)
                r = dfs(root.right)

                if not l and not r:
                    return str(root.val)

                if l and r:
                    return f"{root.val}({l})({r})"

                return f"{root.val}({l})" if l else f"{root.val}()({r})"

        return dfs(root)
