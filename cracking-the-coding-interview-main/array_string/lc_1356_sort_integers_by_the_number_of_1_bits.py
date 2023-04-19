"""
https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explantion: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]
"""
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda a: [bin(a).count('1'), a])
        # Second "a" means:
        # after you made the sort by counting number of 1 bits,
        # you need to get the original list.

    def sortByBitsV2(self, arr: List[int]) -> List[int]:
        temp = []
        for i in arr:
            temp.append([i.bit_count(), i])
        temp.sort()
        return [x[1] for x in temp]
