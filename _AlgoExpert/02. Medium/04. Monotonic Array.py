# O(N) time | O(1) space
def solution2(nums: list) -> bool:
    A = nums
    increasing = decreasing = True

    for i in range(len(A) - 1):
        if A[i] > A[i+1]:
            increasing = False
        if A[i] < A[i+1]:
            decreasing = False

    return increasing or decreasing
