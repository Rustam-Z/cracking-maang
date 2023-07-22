"""
https://leetcode.com/problems/reconstruct-itinerary/

Find lists that start with JFK and take that one that has smallest LEXI order. If used remove from list.

Example 1:
    [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

    # Create adjacency list
    JFK: SFO, ATL
    SFO: ATL
    ATL: JFK, SFO

    # Start from JFK and create a route, update the adjacency list and remove the used element
    ["JFK","ATL"], ["ATL","JFK"], ["JFK","SFO"], ["SFO","ATL"], ["ATL","SFO"]

Example 2:
    [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

    # Create adjacency list, look that SJC doesn't exist as a key
    MUC: LHR
    JFK: MUC
    SFO: SJC
    LHR: SFO

    # Start from JFK and create a route, update the adjacency list and remove the used element
    ["JFK","MUC"], ["MUC","LHR"], ["LHR","SFO"], ["SFO","SJC"]


"""
from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)

        for src in graph.keys():
            graph[src].sort(reverse=True)

        stack = ["JFK"]
        result = []

        while len(stack) > 0:
            # So, what we do here, is creating a route inside the stack.
            element = stack[-1]
            if element in graph and len(graph[element]) > 0:
                # If element is the last one, then it is not present in GRAPH, means we directly append it do result
                stack.append(graph[element].pop())
            else:
                result.append(stack.pop())

        return result[::-1]
