"""
Design ordered stream: https://leetcode.com/problems/design-an-ordered-stream/

Problem:
    There is insert() method, which takes a streamId and a value.
    insert() should return stream values in order, starting from 1.
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
