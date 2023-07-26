"""
Kosaraju's algorithm to find strongly connected components

Algorithm:
    1. Start DFS from vertex 0. Create "Visited set" and "stack".
    2. Visit all of its child vertices, and mark the visited vertices as done.
       If a vertex leads to an already visited vertex, or we reached the end, then push this vertex to the stack.
       Example: 3 -> 0. 0 is already visited. Then push 3 to the stack.
    3. Reverse the graph. Create new visited set. But we will use old stack.
    4. Start from the top vertex (the end) of the stack. Traverse through all of its child vertices. Once the already visited vertex is reached, one strongly connected component is formed.


Applications:
    - Vehicle routing applications
    - Maps

https://www.programiz.com/dsa/strongly-connected-components
"""

from collections import defaultdict


class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)
        self.dfs_data = []
        self.strongly_connected_components = []

    # Add edge into the graph. Directed graph.
    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)

    def dfs(self, node, visited_vertex):
        visited_vertex[node] = True
        self.dfs_data.append(node)
        for i in self.graph[node]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    # To accomplish step 2, we need to fill the stack.
    def fill_order(self, node, visited_vertex, stack):
        visited_vertex[node] = True
        for i in self.graph[node]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack.append(node)

    # Transpose the matrix. Reverse the graph.
    def transpose(self):
        graph = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                graph.add_edge(j, i)

        return graph

    # Print strongly connected components.
    def print_scc(self):
        stack = []
        visited_vertex = [False] * self.V

        # STEP 2: Populate stack.
        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        # STEP 3: Reverse the graph.
        graph = self.transpose()

        visited_vertex = [False] * self.V

        # STEP 4: One by one pop a vertex from stack. And create a strongly connected component.
        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                graph.dfs(i, visited_vertex)

                graph.strongly_connected_components.append(graph.dfs_data)
                graph.dfs_data = []  # Reset the DFS data.

        print(graph.strongly_connected_components)


if __name__ == "__main__":
    g = Graph(8)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 0)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 4)
    g.add_edge(6, 7)

    print("Strongly Connected Components:")
    g.print_scc()
