"""
LeetCode: https://leetcode.com/problems/first-bad-version/

Problem: Given API version as int, find the first version which is bad.

Input: int, last API version
Output: int, first bad version

SOLUTION 1:
    - Binary search
    - But we should sure that the version is bad by checking that the version before bad is good version
    - Time: O()
    - Space: O()
"""


def isBadVersion(version: int) -> bool:
    ...


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    right = mid - 1
            elif not isBadVersion(mid):
                left = mid + 1
