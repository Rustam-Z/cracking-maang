"""
LeetCode: https://leetcode.com/problems/n-th-tribonacci-number/

Problem: Given the two 32-bit numbers, N and M, and two bit position i and j. Write a method to insert M into N such that M starts at bit j and ends at bit i.

Solution:
1. Clear hte bits j through i in N
2. Shift M so that it lines up with bits j through i
3. Merge M and N

Time: O(1)
Space: O(1)
"""


def update_bits(n: int, m: int, i: int, j: int):
    all_ones = ~0  # Will equal sequence of all 1s
    left = all_ones << (j + 1)  # 1s before position j, then 0s, left = 11100000
    right = ((1 << i) - 1)  # right = 00000011
    mask = left | right  # 11100011
    n_cleared = n & mask  # leaving 0s in the middle
    m_shifted = m << i  # preparing m, so that 10011 << 2 is 1001100
    return n_cleared | m_shifted


if __name__ == "__main__":
    res = update_bits(1024, 19, 2, 6)
    print(res)
