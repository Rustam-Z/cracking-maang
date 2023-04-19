"""380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1

Problem:
    Implement RandomizedSet class with 3 methods. insert, remove, and getRandom with O(1) time complexity.
    random.choice(list or tuple) only accepts list or tuple. So, set can't be used.

Constraints:
    - No duplicate numbers
    - If element is present, then don't insert it
    - If element is not present while removing, then return False

Solution:
    - Use list to track of element and hash table for saving the index of values in the list
    - Remove method is tricky here.
        - You need to place the item in the end before removing, as removing in the end is O(1)
        - Don't forget to update the new index of the latest item in list in the hash table
    - Time O(1) for all operations
    - Space O(N) because we use extra memory

"""


import random


class RandomizedSet:
    def __init__(self):
        self.indexes = {}  # value: index in list
        self.values = []  # values, we use in getRandom

    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False

        self.indexes[val] = len(self.values)
        self.values.append(val)

        return True

    def remove(self, val: int) -> bool:
        # We need to swap with the end, because deletion in the end is O(1)
        if val not in self.indexes:
            return False

        index_of_elem_to_remove = self.indexes[val]
        last_elem_in_values = self.values[-1]

        self.indexes[last_elem_in_values] = index_of_elem_to_remove
        self.values[index_of_elem_to_remove] = last_elem_in_values
        self.values[-1] = val

        self.values.pop()
        self.indexes.pop(val)

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


def main():
    obj = RandomizedSet()
    param_1 = obj.insert(1)
    param_2 = obj.remove(2)
    param_3 = obj.insert(2)
    param_4 = obj.remove(1)
    param_5 = obj.insert(2)
    param_6 = obj.getRandom()


if __name__ == "__main__":
    main()
