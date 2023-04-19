"""
Adjacency List (array of linked lists)

An adjacency list represents a graph as an array of linked lists.

The index of the array represents a vertex and
each element in its linked list represents the other vertices that form an edge with the vertex.

Pros of Adjacency List:
    - Memory efficient
    - 01. Easy to find all vertices adjacent to vertex easily
Cons of Adjacency List:
    - Finding is slow because all connected nodes need to be discovered first
"""


class ListNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, number_of_vertices):
        self.V = number_of_vertices
        self.graph = [None] * self.V

    def add_edge(self, node1, node2):
        node = ListNode(node2)
        node.next = self.graph[node1]
        self.graph[node1] = node

        node = ListNode(node1)
        node.next = self.graph[node2]
        self.graph[node2] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print("")


if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_agraph()
