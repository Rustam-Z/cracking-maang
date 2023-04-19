class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                break
        return root

    def lowestCommonAncestorRecursive(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recursion(root, p, q):
            if root == None:
                return
            if root.val < p and root.val < q:
                return recursion(root.right, p, q)
            elif root.val > p and root.val > q:
                return recursion(root.left, p, q)
            else:
                return root

        return recursion(root, p.val, q.val)
