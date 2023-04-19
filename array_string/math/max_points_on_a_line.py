"""149. Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/description/

Approach
    Initially I wanted to use y = kx + b formula to find k=slope and b. But later understood that we only need k, as intercept doesn't affect on number of points. Imagine that b = 0.
    So, everytime I calculate new slope with 2 points and save in plane_points. I update max_points after some change to plane_points was done. It is done because I didn't want to use max(plane_points.values()) later which has O(N) time complexity.

Complexity
    Time complexity: O(N^2)
    Space complexity: O(N)

"""
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        if length < 2:
            return length

        max_points = 1

        for i in range(length - 1):
            if max_points > length - i:
                break

            plane_points = {}

            for j in range(i + 1, length):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 == x2:
                    k = float('inf')
                else:
                    k = (y1 - y2) / (x1 - x2)

                plane_points[k] = plane_points[k] + 1 if k in plane_points else 2
                max_points = max(max_points, plane_points[k])

        return max_points
