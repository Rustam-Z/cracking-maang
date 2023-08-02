"""
Problem: Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
On any order: 1, 2 and 2, 1 are the same.

Example 1:
    Input: n = 4, k = 2
    Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Example 2:
    Input: n = 1, k = 1
    Output: [[1]]
"""


def brute_force(n: int, k: int) -> list:
    """
    Time complexity: O(n^k)
    Space complexity: O(n^k)
    """

    def backtrack(start=1, curr_comb=[]):
        if len(curr_comb) == k:
            output.append(curr_comb[:])
            return

        for i in range(start, n + 1):
            curr_comb.append(i)
            backtrack(i + 1, curr_comb)
            curr_comb.pop()  # Remove the latest element. [1, 2] and give chance to [1, 3].a

    output = []
    backtrack()
    return output


if __name__ == "__main__":
    assert brute_force(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert brute_force(1, 1) == [[1]]
    assert brute_force(4, 1) == [[1], [2], [3], [4]]
