"""
https://leetcode.com/problems/time-based-key-value-store/

Create the data structure similar to key: [(value, timestamp), (value, timestamp)]
    set(key: str, value: str, timestamp: int) -> timestamp will be in ascending order, so you'll have already sorted values.
    get(key: str, timestamp: int) -> return the timestamp_prev from list that is closer to timestamp.

Solution:
    1. Use the defaultdict(list) -> # the key value is the list of (val, timestamp)
    2. O(logN) Binary search can be used because when adding data, the timestamp is already sorted

Time comp: O(logN), time needed for binary search to find closer timestap
Space comp: O(1), not considering space for creating DS
"""
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)  # list of (val, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.map:
            return ''

        # O(logN) Binary search can be used because when adding data, the timestamp is already sorted
        result = ''
        items = self.map[key]  # list of (val, timestamp)

        left, right = 0, len(items) - 1
        while left <= right:
            mid = (right + left) // 2
            if items[mid][1] <= timestamp:
                result = items[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

