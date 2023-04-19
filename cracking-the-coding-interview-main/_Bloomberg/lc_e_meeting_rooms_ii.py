"""Meeting rooms II

Problem: Given starting and ending times of meetings. Return minimum number of rooms we need.

Input: array of meetings with starting and ending times.
Output: number of rooms.

Solution:
    - We could create two arrays, for start and end. Then sort them.
    - Then we use two pointers. 1st for start array, 2nd for end array. We loop over the start array. Till it ends.
    - If start time is smaller than end time. We increment rooms number, and increment start pointer.
    - If start time is bigger than end time, we decrement number of rooms, and we increment end pointer.
    - Time O(N*logN)
    - Space O(N)
"""
from heapq import *


# Time O(N*logN) | Space O(N)
def count_minimum_meeting_rooms(intervals: list) -> int:
    """
    array: [(start, end), (start, end), ...]
    """
    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])

    result, count = 0, 0
    start_ptr, end_ptr = 0, 0

    while start_ptr < len(start):
        if start[start_ptr] < end[end_ptr]:
            start_ptr += 1
            count += 1
        else:
            end_ptr += 1
            count -= 1
        result = max(result, count)

    return count


# Time O(N*logN) | Space O(N)
def solution_using_heap(intervals: list) -> int:
    intervals.sort(key=lambda x: x[0])
    heap = []
    res = 0
    for interval in intervals:
        if len(heap) == 0 or heap[0] > interval[0]:
            res += 1
        else:
            heappop(heap)
        heappush(heap, interval[1])
    return res
