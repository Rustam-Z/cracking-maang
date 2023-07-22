"""
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/

Problem: Merge all overlapping intervals

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

[[1,3],[2,6],[8,10],[15,18]]
[[1,4],[4,5]]
[[1,4],[0,4]] for this reason we need to sort
[[1,4],[2,3]] for this reason we need to save max

Solution 1: sort list, in-place change, and pop, O(N^2) time, O(1) space
Solution 2: sort, use extra space, O(N) time, O(N) space
"""


def solution1(intervals: list) -> list:

    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x[0])

    arr = intervals
    i = 0
    while i < len(intervals) - 1:
        if arr[i][1] >= arr[i + 1][0]:
            arr[i][1] = max(arr[i + 1][1], arr[i][1])
            arr.pop(i + 1)
        else:
            i += 1

    return intervals


def solution2(intervals: list) -> list:
    res = []
    for i in sorted(intervals, key=lambda x: x[0]):
        if res and i[0] <= res[-1][1]:
            res[-1][1] = max(i[1], res[-1][1])
        else:
            res += [i]
    return res
