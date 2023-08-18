"""
https://leetcode.com/discuss/interview-question/1544100/Google-or-Virtual-Interview-or-Test-Engineer

Problem:
    You will be given two inputs N = Number of blocks and L = Length of queue,
    you will have blocks of sizes ranging from 1-8,
    we should return number of ways to fill the queue of length L with exact Number of blocks N.

Example:
    N=2, L=4
    Total 3 ways: 1+3 , 3+1, 2+2
"""


def backtracking_solution(N, L):
    """
    Algorithm:
        - Try all combination of numbers in range of Length of queue. Taking care that length should be number of blocks.
        - If sum of combination is equal to length of queue, increment the count.
    Time complexity: O(N^L)
    Space complexity: O(L)
    """
    output = []

    def backtrack(curr_sum=0, curr_comb=[]):
        if len(curr_comb) == N:
            if curr_sum == L:
                output.append(curr_comb[:])
            return

        for i in range(1, L + 1):
            curr_comb.append(i)
            backtrack(curr_sum + i, curr_comb)
            curr_comb.pop()

    backtrack()
    return output


if __name__ == "__main__":
    print(backtracking_solution(2, 4))
