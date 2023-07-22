"""460. LFU Cache
https://leetcode.com/problems/lfu-cache/description/

int get(int key)
    Gets the value of the key if the key exists in the cache. Otherwise, returns -1.

void put(int key, int value)
    Update the value of the key if present, or inserts the key if not already present.
    When the cache reaches its capacity, it should invalidate and remove
    the least frequently used key before inserting a new item.
    For this problem, when there is a tie (i.e., two or more keys with the same frequency),
    the least recently used key would be invalidated.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation).
The use counter for a key in the cache is incremented either a get or put operation is called on it.

APPROACH:
    Use dict for tracking values.
    Use dict for tracking counter for each key.
    Use dict for tracking counter and the keys list.
        It will be used to find the least frequently used keys.
        And will be used for removing keys when we reach capacity.
"""

from collections import defaultdict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = dict()  # key: value
        self.counter_key = defaultdict(list)
        self.key_counter = dict()
        self.min_counter = float("inf")

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        value_to_return = self.values[key]
        self.update_frequency(key)
        return value_to_return

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key not in self.values:
            if len(self.values) >= self.capacity:
                # Need to remove the least frequently and recently used.
                # How?
                # We need to get the smallest counter in counter_key, and remove the least recently used,
                # that is the FIRST one, let's imagine that pop os O(1)
                self.min_counter = min(self.counter_key)
                key_to_remove = self.counter_key[self.min_counter][0]
                del self.counter_key[self.min_counter][0]
                del self.values[key_to_remove]
                del self.key_counter[key_to_remove]

            self.key_counter[key] = 1
            self.counter_key[1].append(key)
            self.min_counter = 1
        else:
            self.update_frequency(key)

        self.values[key] = value

    def update_frequency(self, key):
        counter = self.key_counter[key]
        self.key_counter[key] += 1

        self.counter_key[counter].remove(key)
        self.counter_key[counter + 1].append(key)

        if not self.counter_key[counter]:
            del self.counter_key[counter]

        self.min_counter = min(self.min_counter, counter + 1)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
