"""452. Minimum Number of Arrows to Burst Balloons
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

Problem:
    Given the balloons in XY plane, you only know X start and end coordinated,
    you need to burst them with minimum number of shots.
"""
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        result, curr_start = 1, points[-1][0]
        for start, end in reversed(points):
            if end < curr_start:
                curr_start = start
                result += 1
        return result

