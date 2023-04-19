import heapq
from collections import defaultdict, Counter
from typing import List


class Solution:
    # O(N*logN) time | O(n) space
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Use heap data structure
        heapq
        nlargest
        """
        frequency = Counter(words)
        top_k = heapq.nlargest(k, sorted(frequency.items()), key=lambda x: x[1])
        # We use sorted because it is said to keep lexicographic order
        return [i[0] for i in top_k]

    # O(N*logN) time | O(n) space
    def topKFrequentBetter(self, words: List[str], k: int) -> List[str]:
        # Count
        counts = defaultdict(int)
        for word in words:
            counts[word] += 1

        # Add to heap
        counts_heap = []
        for word, count in counts.items():
            heapq.heappush(counts_heap, (-count, word))

        # Select Top k
        result = []
        while k != 0:
            _, word = heapq.heappop(counts_heap)
            result.append(word)
            k -= 1

        return result
