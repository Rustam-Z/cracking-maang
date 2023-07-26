"""
https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

Problem:
    - Given a list of distances, and a time, find the minimum speed to arrive on time.

Constraints:
    - Trains leave only at integer hours. So if you arrived at 1.5 hours, you'll have to wait for 2 hours. So we use ceil.

Input: dist = [1,3,2], hour = 6
Output: 1
Explanation: At speed 1:
    - The first train ride takes 1/1 = 1 hour.
    - Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3 hours.
    - Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
    - You will arrive at exactly the 6 hour mark.

Solution:
    - We can use binary search to find the smallest feasible speed.
    - If the speed is feasible, then we can try to find a smaller speed.
    - If the speed is not feasible, then we can try to find a larger speed.

Time complexity: O(NlogM), where N is the length of dist, and M is the maximum distance in dist.
Space complexity: O(1)
"""
from math import ceil
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1

        # A function to check if a certain speed is feasible.
        def speedcheck(speed):
            time = 0
            for i in range(len(dist) - 1):
                time += ceil(dist[i] / speed)
            time += dist[-1] / speed
            if time <= hour:
                return True

        min_speed = 1
        max_speed = 10 ** 7

        while min_speed < max_speed:
            mid_speed = (min_speed + max_speed) // 2

            if speedcheck(mid_speed):
                max_speed = mid_speed
            else:
                min_speed = mid_speed + 1

        return min_speed
