# Heap
- Also called a priority queue.
- It is a complete binary tree
- https://www.programiz.com/dsa/heap-data-structure


## Heap implementation in Pythno
- https://docs.python.org/3/library/heapq.html
- Python's heapq module implements a min-heap.
- `heapq.heappush(heap, item`) - Push the value item onto the heap, maintaining the heap invariant. 
  - Use `heapfiy()`, if array is not empty and was not heapified before.
  - Use `heappushpop()`, if you would like to push and pop the smallest element.
  - If array is empty you can use `heappush()` to add new item. No need to use `heapify()` in this case.
- `heapq.heappop(heap)` - Pop and return the smallest item from the heap, maintaining the heap invariant. 
  - Use `heapfiy()`, before using `heappop()`. Otherwise you will get only first elements.

```python
heapq.heapify(list)  # O(N), in-place operation, min heap by default.
heapq.heappush(heap, item)  # O(logn), push the value item onto the heap, maintaining the heap invariant.
heapq.heappop(heap)  # O(logn)
heapq.nlargest(n, iterable, key=None) # O(k*log(k)) to find the K largest element
heapq.nsmallest(n, iterable, key=None)
```

```python
# If you would like to convert an existing array / list to a heap, then use the heapify method
import heapq
heap = [3, 2, 1, 5, 9, 7, 4, 6, 8]

heapq.heapify(heap)
print(heap[0]) 
```

```python
# Max heap.
from heapq import *

h = [5, 7, 9, 1, 3]
h_neg = [-i for i in h]

heapify(h_neg)       # heapify
heappush(h_neg, -2)  # push
-heappop(h_neg)      # pop, 9
```

```python
def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
    counts = Counter(nums) # Counter({'i': 2, 'love': 2, 'leetcode': 1, 'coding': 1})
    top_k = heapq.nlargest(k, counts.items(), key=lambda x: x[1]) # [["i",2],["love",2]]
    return [i[0] for i in top_k]
```

```python
# How heapsort works with heapq module
def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for _ in range(len(h))]
heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

```python
# if you would like to keep the heap property of your data structure when adding new elements, then heappush is a way to go
import heapq 
q = []

heapq.heappush(q, (2, 'code')) # no need to use heapfiy, because heappush maintains the structure of heap
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))

while q:
    next_item = heapq.heappop(q)
    print(next_item)
    
# Result:
# (1, 'eat')
# (2, 'code')
# (3, 'sleep')
```
