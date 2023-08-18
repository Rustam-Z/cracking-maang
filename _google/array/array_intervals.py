from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge Intervals: https://leetcode.com/problems/merge-intervals/

    Problem:
        Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
        and return an array of the non-overlapping

    Constraints and clarifications:
        - Can we assume that the intervals are sorted?
        - What if we have less than 2 intervals?

    Algorithm:
        - Sort the intervals by the start time
        - Iterate through the intervals
            - If the current interval's end time is greater than the next interval's start time
            - Update the current interval's end time to be the max of the two
            - Remove the next interval

    Time complexity: O(nlogn)
    Space complexity: O(n)
    """

    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x[0])

    arr = intervals  # Because we need it in the while loop
    i = 0
    while i < len(intervals) - 1:
        if arr[i][1] >= arr[i + 1][0]:
            arr[i][1] = max(arr[i + 1][1], arr[i][1])
            arr.pop(i + 1)
        else:
            i += 1

    return intervals


def insert_intervals(intervals: list, new_interval: list) -> list:
    """
    Insert Interval: https://leetcode.com/problems/insert-interval/

    Problem:
        Insert interval, and return merged.

    Constraints:
        - Can we assume that the intervals are sorted?
        - New interval is not empty? Will it contain only 1 interval?
        - Integer questions: range?

    Brute force algorithm:
        - Sort the intervals by the start time
        - Insert the new interval
        - Merge the intervals
        Time complexity: O(nlogn)
        Space complexity: O(n)

    Optimized solution:
        - Find the index where the new interval should be inserted
        - Merge the intervals
        Time complexity: O(n)
        Space complexity: O(n)
    """

    def brute_force(intervals: list, new_interval: list) -> list:
        intervals.append(new_interval)
        intervals.sort(key=lambda x: x[0])
        return merge_intervals(intervals)

    def optimized_solution(intervals: list, new_interval: list) -> list:
        i = 0
        while i < len(intervals) and intervals[i][0] < new_interval[0]:
            i += 1

        intervals.insert(i, new_interval)
        return merge_intervals(intervals)

    def another_one(intervals: list, new_interval: list) -> list:
        # Time complexity: O(n)
        # Space complexity: O(n)

        intervals.append(new_interval)
        # Sort the intervals array by start
        intervals.sort(key=lambda x: x[0])
        # Initialize an empty result array
        result = []
        # Iterate through the intervals array
        for interval in intervals:
            # If the result array is empty, append the current interval
            if not result:
                result.append(interval)
            else:
                if result[-1][1] >= interval[0]:
                    result[-1][1] = max(result[-1][1], interval[1])
                # Otherwise, append the current interval
                else:
                    result.append(interval)
        return result
