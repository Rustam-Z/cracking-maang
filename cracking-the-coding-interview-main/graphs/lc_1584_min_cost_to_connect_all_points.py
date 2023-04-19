"""
LeetCode: 1584. Min Cost to Connect All Points, https://leetcode.com/problems/min-cost-to-connect-all-points/

Problem: Minimum spanning tree. Given a set of points on a 2D plane, find the minimum cost to make,

Solution:
1. Use the Prim's algorithm to find the minimum spanning tree.

Time: O(n^2 * logn)
Space: O()
"""
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = [[] for _ in range(N)]  # i : list of [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's algorithm
        # 1. Initialize the set of visited nodes to be empty.
        # 2. Assign a key value to each node in the graph.

        res = 0
        visited = set()
        minH = [[0, 0]]
        while len(visited) < N:
            cost, i = heapq.heappop(minH)
            if i in visited:
                continue
            visited.add(i)
            res += cost
            for neighCost, j in adj[i]:
                if j not in visited:
                    heapq.heappush(minH, [neighCost, j])

        return res
