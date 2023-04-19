"""1029. Two City Scheduling
https://leetcode.com/problems/two-city-scheduling/

Problem:
    A company is planning to interview 2n people.
    Given the array costs where costs[i] = [aCosti, bCosti],
    the cost of flying the ith person to city a is aCosti,
    and the cost of flying the ith person to city b is bCosti.
    Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

Input: costs array, where costs[i] = [aCosti, bCosti]
Output: int, minimum cost

Constraints:
    - The length of input array is even.
    - n people should arrive in each city.

Solution:
    - Sort the array depending on the diffrence cost.
    - Then the half of items is for city A, the next half is for city B
"""
from typing import List


def twoCitySchedCost(costs: List[List[int]]) -> int:
    total = 0
    half = len(costs) // 2  # len(costs) is always even
    # For city A, take half MIN nums
    # For city B, take rest, meaning half of MAX nums
    # Better to sort
    costs.sort(key=lambda x: x[0] - x[1])

    counter = 0
    while counter < half:
        total += costs[counter][0] + costs[counter + half][1]
        counter += 1

    return total

