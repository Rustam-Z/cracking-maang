class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        return 0 if not root else max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1
