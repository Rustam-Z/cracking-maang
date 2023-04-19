"""1519. Number of Nodes in the Sub-Tree With the Same Label
https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/description/

NOTE!
    [[0,2],[0,3],[1,2]
    The edge [1,2] does not necessarily mean that node 1 is the parent of 2, but that there exists an edge between them.
     0
   /   \
  3     2
         \
          1


Approach:
    - Use DFS algorithm, create an adjacency list to save all <-> edges between vertices.
    - We need to have a visited set. So that we don't need to revisit the node which was visited already.
    - We will use a dictionary to remember what kind of labels the children had.
    - Time: O(N)
    - Space: O(N)

"""
from collections import defaultdict
from typing import List


class Solution:

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adjacency_list = defaultdict(list)

        for node1, node2 in edges:
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)

        visited_nodes = set()
        result = [None] * n

        def dfs(cur_node: int) -> dict:
            visited_nodes.add(cur_node)
            cur_node_label = labels[cur_node]
            current_node_mapping = defaultdict(int)
            current_node_mapping[cur_node_label] += 1

            for child in adjacency_list[cur_node]:
                if child in visited_nodes:
                    continue

                child_mapping = dfs(child)
                # Update current_node_mapping with child_mapping
                for key, value in child_mapping.items():
                    current_node_mapping[key] += value

            result[cur_node] = current_node_mapping.get(cur_node_label)
            return current_node_mapping

        dfs(0)
        return result
