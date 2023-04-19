class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()

        queue.append(p)
        queue.append(q)

        while queue:
            p = queue.popleft()
            q = queue.popleft()

            if p is None and q is None:
                continue

            if p is None or q is None:
                return False

            if p.val != q.val:
                return False

            queue.append(p.left)
            queue.append(q.left)
            queue.append(p.right)
            queue.append(q.right)

        return True
