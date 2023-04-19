"""
To save the structure of Max Heap, we used negative numbering.

For examole:
h = [5, 7, 9, 1, 3]
h_neg = [-i for i in h]

heapify(h_neg)            # heapify
heappush(h_neg, -2)       # push
print(-heappop(h_neg))    # pop
"""

import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            e1 = -heapq.heappop(heap)
            e2 = -heapq.heappop(heap)
            print(e1, e2)

            if e1 != e2:
                ins = e2 - e1  # Because now order of max heap changed
                heapq.heappush(heap, ins)

            print(heap)
        return -heap[0] if heap else 0
