"""1656. Design an Ordered Stream
https://leetcode.com/problems/design-an-ordered-stream/

Problem: Values are inserted randomly in any index. The ptr is in the start by default.
    Return the continuous stream if it is filled. Then put the ptr to first unfilled index.

Constraint:
    - No duplicate keys
    - Values are strings
    - Keys are integers
    - The length of array will be provided

Solution:
    - Using the array data structure. And track the ptr.
    - Insertion: insert the value in list. Then loop over each item from prt.
        If unfilled index is found then change ptr to point to that index.
"""
from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.filled_indexes = [None] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        result = []

        self.filled_indexes[idKey] = value

        for i in range(self.ptr, len(self.filled_indexes)):
            if self.filled_indexes[i] is None:
                self.ptr = i
                break

            result.append(self.filled_indexes[i])

        return result


def main():
    test_data = [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]

    obj = OrderedStream(test_data[0][0])
    for i in range(1, len(test_data)):
        result = obj.insert(test_data[i][0], test_data[i][1])
        print(result)


if __name__ == "__main__":
    main()
