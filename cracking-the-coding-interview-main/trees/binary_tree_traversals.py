class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Traverse:
    def traversal(self, type_of_dfs: str, root: TreeNode) -> list:
        traversed_tree = []
        args = root, traversed_tree

        traversals = {
            "inorder": self.inorder_traversal,
            "preorder": self.preorder_traversal,
            "postorder": self.postorder_traversal
        }

        traversals[type_of_dfs](*args)

        return traversed_tree

    def preorder_traversal(self, root, traversed_tree):
        if root:
            # NLR
            traversed_tree.append(root.val)
            self.preorder_traversal(root.left, traversed_tree)
            self.preorder_traversal(root.right, traversed_tree)

    def inorder_traversal(self, root, traversed_tree):
        if root:
            # LNR
            self.inorder_traversal(root.left, traversed_tree)
            traversed_tree.append(root.val)
            self.inorder_traversal(root.right, traversed_tree)

    def postorder_traversal(self, root, traversed_tree):
        if root:
            # LRN
            self.postorder_traversal(root.left, traversed_tree)
            self.postorder_traversal(root.right, traversed_tree)
            traversed_tree.append(root.val)


if __name__ == "__main__":
    node3 = TreeNode(3)
    node2 = TreeNode(2)
    node1 = TreeNode(1, node2, node3)

    traverse = Traverse()

    inorder_traversal = traverse.traversal("inorder", node1)
    preorder_traversal = traverse.traversal("preorder", node1)
    postorder_traversal = traverse.traversal("postorder", node1)

    print("Inorder:", inorder_traversal)
    print("Preorder:", preorder_traversal)
    print("Postorder:", postorder_traversal)
