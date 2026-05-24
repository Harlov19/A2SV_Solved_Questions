class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)

        heap = []

        for word, count in freq.items():
            heapq.heappush(heap, (-count, word))

        heap.sort()

        return [word for _, word in heap[:k]]
