"""
Heap (priority queue)

https://realpython.com/python-heapq-module/

Its first child is at 2*k + 1.
Its second child is at 2*k + 2.
Its parent is at (k - 1) // 2.

heapify() is used to turn to the heap
heappop() pop and return the smallest element from heap
heappush() to push to the end

"""
from heapq import heappop, heappush, heapify


class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        """
        Method to take the parent of any node.
        :param i: child node from which you want to find its parent.
        :return:
        """
        return (i - 1) / 2

    def insert_key(self, k):
        """
        Method to insert a value to heap.
        :param k:
        :return:
        """
        heappush(self.heap, k)

    def extract_min(self):
        """
        Method to remove the min element from heap.
        :return: heap
        """
        return heappop(self.heap)

    def get_min(self):
        """
        Get the minimum element from the heap
        :return:
        """
        return self.heap[0]

