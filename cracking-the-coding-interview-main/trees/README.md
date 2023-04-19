# [Trees](https://github.com/Rustam-Z/data-structures-and-algorithms#tree)

### Questions to raise during coding interview
1. Trees / binary tree
2. Binary tree / binary search tree
3. If BST do we have duplicates? And in which side?
4. Balanced (AVL tree) / unbalanced. Balanced doesn't mean having exact same size in left and right size. It means "not terribly unbalanced" and ensures `O(log n)` for insert and find.

### Types of binary trees
1. Complete binary tree = every level of the tree is fully filled, except for perhaps the last level. Filled left to right.
2. Full binary tree = every node has either zero or two children.
3. Perfect binary tree = all leaf nodes at the same level, both full and complete. `len = 2^k - 1`, where `k` is depth of tree. 
4. Binary search tree = ordered binary tree. L < N <= R.
5. Balanced binary tree = difference between the left and the right subtree for any node is not more than one.
6. [AVL Tree](https://www.programiz.com/dsa/avl-tree) = self-balancing binary search tree in which each node maintains extra information called a balance factor whose value is either -1, 0 or +1.
7. [B-tree](https://www.programiz.com/dsa/b-tree) = self-balancing search tree in which each node can contain more than one key and can have more than two children. Generalized form of the binary search tree.
8. [B+ tree](https://www.programiz.com/dsa/b-plus-tree) = self-balancing tree in which all the values are present in the leaf level, children of red node are black, number of black nodes for each node is the same.
9. [Red-black tree](https://www.programiz.com/dsa/red-black-tree) = root is black, 

### Notes on binary trees (page 102)
1. **Edge** = link between any two nodes.
2. **Height of node** = number of edges from the deepest leaf to node.
3. **Depth of a node** = number of edges from the root to the node.
4. **Height of a tree** = height of the root node.
5. If TREE[0] = ROOT then
    - Left child of a node K => `2*K + 1`
    - Right child of a node K => `2*K + 2`
    - Parent of any node K => `floor(K/2) - 1`
6. DFS Traversals: pre-order (NLR), post-order (LRN), in-order (LNR)
    - When we perform in-order traversal on BST, it visits the nodes in ascending order.
    - In pre-order the root is always visited first.
    - In post-order the root is always the last node visited.

### Binary heaps (min-heap)
1. A min-heap is a complete binary tree where each node is smaller than its children. The root = min element in tree.
2. We have two methods, `insert()` and `extract_min()`, both `O(logn)`, where `n` is the number of nodes in the heap.


897 - beautiful use case of in-order traversal
ctci_4.5_validate_BST.py - traversal with arg