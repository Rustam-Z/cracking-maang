# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        Solution:
        - The problem is to create a path from any node to its children. And find max absolute difference.
        - DFS or BFS?
        - If BFS, then level by level: track, max and min values. 
          - Then everytime, try to calcualte the new difference. 
        """

        maxVal = 0
        queue = deque([(root, root.val, root.val)])

        while queue:
            curr, high, low = queue.popleft()
            maxVal = max(maxVal, abs(curr.val - low), abs(high - curr.val))

            if curr.left:
                queue.append((curr.left, max(curr.val, high), min(curr.val, low)))
            if curr.right:
                queue.append((curr.right, max(curr.val, high), min(curr.val, low)))

        return maxVal
    
