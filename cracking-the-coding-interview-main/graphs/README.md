# [Graphs](https://github.com/Rustam-Z/data-structures-and-algorithms#graphs)

### Graph
- Vertices = nodes, edges = lines between vertices, adjacent vertices = there is an edge (link) between them 
- Graph is a collection of nodes with edges between some of them.
- Tree is a graph, but not all graphs are trees. Tree is connected graph without cycles.
- Graph can be represented as adjacency matrix (2D array) or adjacency list (array of linked lists).
- **Directed** = one way street, **undirected graph** = two-way street, do not point to any direction.
- **Connected graph** = undirected graph in which there is always a path from a vertex to any other vertex.
- **Strongly connected graph** = directed graph (one way edges) in which there is a route between every two nodes.
- [**Spanning tree**](https://www.programiz.com/dsa/spanning-tree-and-minimum-spanning-tree) = a sub-graph of an undirected connected graph, which includes **all** the vertices of the graph with a minimum possible number of edges. 
  - Example: computer network routing protocol.
- **Minimum spanning tree** = A minimum spanning tree is a spanning tree in which the sum of the weight of **all edges** is as minimum as possible.
  - Example: to find paths in the map, to design networks like telecommunication networks, water supply networks, and electrical grid.
- **Shortest path** differs from the minimum spanning tree because the shortest distance between two vertices might not include all the vertices of the graph.

### Graph algorithms
- DFS (depth first search), stack
- BFS (breadth first search), queue
- Dijkstra's algorithm (The shortest path) = works in both directed and undirected
- Prim's algorithm (Minimum spanning tree)
  - Works in undirected and connected
  - Runs faster for dense graphs 
  - Visits node more than once
  - Time complexity of O(V2), V being the number of vertices and can be improved up to O(E logV) using Fibonacci heaps
  - Example: travelling salesman problem, network for roads
  - Prim’s algorithm prefer list data structures
- Kruskal's algorithm (Minimum spanning tree)
  - Works in undirected and disconnected nodes also
  - Runs faster for sparse graph
  - You have more control when same weight occurs
  - Visits node only once
  - Time complexity is O(E logV), V being the number of vertices
  - Example: LAN connection, TV Network
  - Kruskal’s algorithm prefer heap data structures
- [Kosaraju's algorithm](https://www.programiz.com/dsa/strongly-connected-components) (Strongly connected component) = finding portion of a directed graph in which there is a path from each vertex to another vertex
  - Perform a depth first search on the whole graph
  - Reverse the original graph
  - Perform depth-first search on the reversed graph

### DFS
- DFS is often preferred if we want to visit every node in the graph
- It is a bit simpler
- Will not find the shortest path

### BFS
- Shortest path between two nodes
- Example: find a path of friendship between A and B. DFS will do deep. But with BFS, we will stay close to nodes neighbors. We will not go to distant connections until absolutely necessary.
