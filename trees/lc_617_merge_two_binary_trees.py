class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None:
            return root2

        if root2 is None:
            return root1

        root1.val = root1.val + root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1


node3 = TreeNode(3)
node2 = TreeNode(2)
node1 = TreeNode(1, node2, node3)

node13 = TreeNode(3)
node12 = TreeNode(2)
node11 = TreeNode(1, node12, node13)

sol = Solution()
print(sol.mergeTrees(node1, node11))
