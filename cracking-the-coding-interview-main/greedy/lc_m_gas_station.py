"""134. Gas Station
https://leetcode.com/problems/gas-station/description/

Problem: I am free to start at any gas station, I need to verify if I can make a round trip.
    I can fill my gas tank to gas[i] at `gas[i]` station.
    And it costs me cost[i] to travel from `i` to `i+1`.

Solution:
    Logically, if sum(gas) > sum(cost) then i can travel.
    Logically, if I'm free to start at any gas station. I will have the gas to make a circle trip.

Time: O(N)
Space: O(1)

"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        # Start at the first gas station
        start = 0
        balance = 0
        for i in range(len(gas)):
            balance += gas[i] - cost[i]
            if balance < 0:
                start = i + 1
                balance = 0

        return start
