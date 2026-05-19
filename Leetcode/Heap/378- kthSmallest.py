class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        heap = []

        
        for row in range(min(n, k)):
            heapq.heappush(heap, (matrix[row][0], row, 0))

        
        for _ in range(k - 1):
            value, row, col = heapq.heappop(heap)

            
            if col + 1 < len(matrix[row]):
                heapq.heappush(
                    heap,
                    (matrix[row][col + 1], row, col + 1)
                )

        return heapq.heappop(heap)[0]
