"""
Problem:
    Given a binary tree, find its maximum depth.

Questions and clarifications:
    - What is the definition of depth?
    - Is it a binary search tree?
"""


def dfs_solution(root):
    """
    Algorithm:
        - DFS to find the depth of each node
        - return the max depth

    Time complexity: O(n)
    Space complexity: O(n)
    """

    def dfs(node):
        if not node:
            return 0
        return max(dfs(node.left), dfs(node.right)) + 1

    return dfs(root)


def bfs_solution(root):
    """
    Algorithm:
        - BFS to find the depth of each node
        - return the max depth

    Time complexity: O(n)
    Space complexity: O(n)
    """

    if not root:
        return 0

    queue = [root]
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth
