class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, value):
        self.children.append(Node(value))

    # O(V+E) time | O(V) space
    def dfs(self, array):
        array.append(self.value)
        for child in self.children:
            child.dfs(array)
        return array

    # O(V+E) time | O(V) space, V = number of vertices (nodes), E = edges (connections)
    def dfs_v2(self):
        result = []

        def dfs(node):
            result.append(node.value)
            for child in node.children:
                dfs(child)

        dfs(self)
        return result
