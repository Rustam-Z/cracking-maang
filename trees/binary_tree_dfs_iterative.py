"""
https://www.techiedelight.com/preorder-tree-traversal-iterative-recursive/
"""

from collections import deque


def preorder_iterative(root):
    if root is None:
        return

    stack = deque()
    stack.append(root)

    while stack:
        curr = stack.pop()
        print(curr.val, end=' ')  # CHANGE

        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)


def preorder_iterative_optimized(root):
    # We push only right child to stack
    if root is None:
        return

    stack = deque()
    stack.append(root)

    curr = root
    while stack:
        if curr:
            print(curr.val, end=' ')  # CHANGE

            if curr.right:
                stack.append(curr.right)
            curr = curr.left
        else:
            curr = stack.pop()


def inorder_iterative(root):
    stack = deque()

    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            print(curr.val, end=' ')  # CHANGE
            curr = curr.right


def postorder_iterative(root):
    if root is None:
        return

    stack = deque()
    stack.append(root)

    # create another stack to store postorder traversal
    out = deque()

    while stack:
        curr = stack.pop()
        out.append(curr.data)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)

    # print postorder traversal
    while out:
        print(out.pop(), end=' ')  # CHANGE
