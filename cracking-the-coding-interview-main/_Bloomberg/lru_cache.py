"""146. LRU Cache
https://leetcode.com/problems/lru-cache/

Problem: Create least recently used data structure.
    get() -> after fetching the value, place the item to the end again.
    put() -> remove from start if size is big. And place item to the end.
"""
import collections


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1

        self.values[key] = self.values.pop(key)  # To keep the key in the end
        return self.values[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.values:
            if len(self.values) >= self.capacity:
                self.values.popitem(last=False)  # If we are out of capacity, we remove the first item in dict
        else:
            self.values.pop(key)

        self.values[key] = value
