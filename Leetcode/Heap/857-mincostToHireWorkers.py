class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        workers = []
        
        for q, w in zip(quality, wage):
            workers.append((w / q, q))
        
        workers.sort()
        
        max_heap = []
        quality_sum = 0
        
        answer = float('inf')
        
        for ratio, q in workers:
            
            heapq.heappush(max_heap, -q)
            quality_sum += q
            
            if len(max_heap) > k:
                quality_sum += heapq.heappop(max_heap)
            
            if len(max_heap) == k:
                answer = min(answer, quality_sum * ratio)
        
        return answer
