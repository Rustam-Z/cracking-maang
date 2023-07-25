"""
Heap sort algorithm implementation.
Largest element is stored at the root of the heap in max heap.

Time complexity: best, worst, average = O(n log n)
Space complexity: O(1)
"""
from heapq import heappush, heappop


def heap_sort_heapq(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for _ in range(len(h))]


def heapify(arr, n, i):
    """
    arr: array to heapify
    n: size of heap, number of elements in the array that need to be heapified.
    i: index of root to which we want to perform heapify.
    """
    largest = i  # Initialize largest as root
    left = 2*i + 1
    right = 2*i + 2

    # See if left child of root exists and is greater than root.
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child of root exists and is greater than root.
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root is not largest, swap with largest and continue heapifying.
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # heapify root element
        heapify(arr, i, 0)


if __name__ == "__main__":
    unsorted_array = [12, 11, 13, 5, 6, 7]
    heap_sort(unsorted_array)
    print(unsorted_array)
