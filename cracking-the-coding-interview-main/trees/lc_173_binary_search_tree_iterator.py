"""
LeetCode: 173. Binary Search Tree Iterator, https://leetcode.com/problems/binary-search-tree-iterator/

Problem: Given the tree, use the inorder traversal

Solution 1:
1. Use the pre-defined in-order
Time: O(n)
Space: O(n)

Solution 2:
1. Use Python generators
Time: O(x) x is the number of next calls we make
Space: O(1)

"""


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]) -> None:
        self._traversal = []
        self._inorder(root)
        self._current = 0

    def _inorder(self, node: Optional[TreeNode]) -> None:
        if node is None:
            return
        self._inorder(node.left)
        self._traversal.append(node)
        self._inorder(node.right)

    def next(self) -> int:
        node = self._traversal[self._current]
        self._current += 1
        return node.val

    def hasNext(self) -> bool:
        return self._current < len(self._traversal)


class BSTIterator2:
    def __init__(self, root: Optional[TreeNode]):
        self.iter = self._inorder(root)
        self.nxt = next(self.iter, None)

    def _inorder(self, node: Optional[TreeNode]) -> Generator[int, None, None]:
        if node:
            yield from self._inorder(node.left)
            yield node.val
            yield from self._inorder(node.right)

    def next(self) -> int:
        res, self.nxt = self.nxt, next(self.iter, None)
        return res

    def hasNext(self) -> bool:
        return self.nxt is not None
