"""
378. Kth Smallest Element in a Sorted Matrix
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Problem: given matrix, each row and column sorted in ascending order, return kth smallest element.

Solution 1: flast the matrix in list, sort the list, return the k-1 item, O(N*logN) time, O(NO space
Solution 2: flat the matrix, min heapify, then pop from heap, O(N) time, O(N) space
Solution 3: use max heap, heappush to heap, and pop when len(heap) is larger than k O(N*logN) time, O(k) space
"""


def solution1(matrix: list, k: int) -> int:
    arr = []
    for i in range(len(matrix)):
        arr.extend(matrix[i])
    arr.sort()
    return arr[k - 1]


def solution2(matrix: list[list[int]], k: int) -> int:
    heap = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            item = matrix[c][r]
            heap.append(item)

    heapq.heapify(heap)  # O(N)

    for i in range(k - 1):
        heapq.heappop(heap)

    return heapq.heappop(heap)


def solution3(matrix: list[list[int]], k: int) -> int:
    heap = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            item = -matrix[r][c]
            heapq.heappush(heap, item)

            while len(heap) > k:
                heapq.heappop(heap)

    return -heapq.heappop(heap)
