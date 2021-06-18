"""
TODO: https://leetcode.com/problems/merge-two-binary-trees/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1, root2):
        root1, root2 = self.pad_roots(root1, root2)
        root3 = []

        for i, j in zip(root1, root2):
            # print(i, j)
            if i == None:
                root3.append(j)
            elif j == None:
                root3.append(i)
            elif i == None and j == None:
                root3.append(None)
            else:
                root3.append(i + j)

        return root3

    def pad_roots(self, root1, root2):
        # Make the length of both roots the same
        max_length = max(len(root1), len(root2))

        while len(root1) != max_length:
            root1.append(None)

        while len(root2) != max_length:
            root2.append(None)

        return root1, root2
        

root1 = [1,3,2,5]
root2 = [2,1,3,None,4,None,7]
# root1 = [1]
# root2 = [1,2]
sol = Solution()
print(sol.mergeTrees(root1, root2))