"""
Minimum Cost to Complete Trip, Min round trip cost.
https://stackoverflow.com/questions/69995292/algorithm-question-finding-the-cheapest-flight
"""


def brute_force(D, R):
    """
    Time complexity: O(N^2)
    Space complexity: O(1)
    """
    n = len(D)
    min_cost = float('inf')  # Initialize with a large value

    for i in range(n):
        for j in range(i, n):
            cost = D[i] + R[j]
            min_cost = min(min_cost, cost)

    return min_cost


def optimized_solution(D, R):
    """
    Algorithm:
    - Create a queue with the same length as R.
    - Find the minimum of return cost for each element of R.

    Time complexity: O(N)
    Space complexity: O(N)
    """
    queue = [0] * len(R)

    # Find the minimum of return cost for each element of R.
    queue[-1] = R[-1]
    for i in range(len(R) - 2, -1, -1):
        queue[i] = min(queue[i + 1], R[i])

    # Calculate the best cost.
    best = R[0] + D[0]
    for i, el in enumerate(D):
        best = min(best, D[i] + queue[i])

    return best


if __name__ == "__main__":
    D = [10, 7, 15, 12, 4]
    R = [5, 12, 9, 10, 12]

