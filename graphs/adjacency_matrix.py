"""
Adjacency Matrix (2D array)

An adjacency matrix is a way of representing a graph as a matrix of booleans (0's and 1's).

Each cell in the above table/matrix is represented as Aij, where i and j are vertices.
The value of Aij is either 1 or 0 depending on whether there is an edge from vertex i to vertex j.

Pros of Adjacency Matrix:
    - Adding, checking whether there is an edge from vertex i to vertex j are in O(1)
    - If graph is dense (with many connections)
Cons of Adjacency Matrix:
    - VxV space requirement
"""


class Graph(object):
    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            print(row)


def main():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    g.print_matrix()


if __name__ == '__main__':
    main()
