class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        events = []

        for left, right, height in buildings:
            events.append((left, -height, right))  
            events.append((right, 0, 0))           

        events.sort()

        res = [[0, 0]]

        heap = [(0, float('inf'))]

        for x, neg_h, right in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)

            if neg_h:
                heapq.heappush(heap, (neg_h, right))

            current_height = -heap[0][0]

           
            if res[-1][1] != current_height:
                res.append([x, current_height])

        return res[1:]
