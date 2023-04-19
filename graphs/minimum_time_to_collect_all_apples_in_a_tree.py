"""1443. Minimum Time to Collect All Apples in a Tree
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/

NOTE!
    [[0,2],[0,3],[1,2]
    The edge [1,2] does not necessarily mean that node 1 is the parent of 2, but that there exists an edge between them.
     0
   /   \
  3     2
         \
          1


Approach:
    - DFS Graph Algorithm
    - adjacency_list for edges should be bidirectional. Like (a, b) and (b, a).
      We will have a visited set, the nodes that are visisted will not be visited twice.

"""
from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        adjacency_list = defaultdict(list)

        # Build adjacency list to represent the graph
        for src_node, dst_node in edges:
            adjacency_list[src_node].append(dst_node)
            adjacency_list[dst_node].append(src_node)

        # Record of visited nodes
        visited = set()

        def collect_in_dfs(cur_node):
            visited.add(cur_node)
            cost_of_collect = 0

            for child_node in adjacency_list[cur_node]:
                if child_node in visited:
                    continue

                cost_from_child = collect_in_dfs(child_node)
                if cost_from_child or hasApple[child_node]:
                    # cur_node to child_node, and the second +1 is for going back.
                    cost_of_collect += cost_from_child + 2

            return cost_of_collect
