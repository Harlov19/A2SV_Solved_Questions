class Solution:
    def medianSlidingWindow(self, nums, k):
        
        small = []  
        large = [] 
        delayed = defaultdict(int)
        small_size = 0
        large_size = 0

        def prune(heap):
            while heap:
                x = -heap[0] if heap is small else heap[0]
                if delayed[x]:
                    delayed[x] -= 1
                    heappop(heap)
                else:
                    break
                    
        def rebalance():
            nonlocal small_size, large_size

            if small_size > large_size + 1:
                heappush(large, -heappop(small))
                small_size -= 1
                large_size += 1
                prune(small)

            elif small_size < large_size:
                heappush(small, -heappop(large))
                large_size -= 1
                small_size += 1
                prune(large)

        def add(num):
            nonlocal small_size, large_size

            if not small or num <= -small[0]:
                heappush(small, -num)
                small_size += 1
            else:
                heappush(large, num)
                large_size += 1

            rebalance()

        def remove(num):
            nonlocal small_size, large_size

            delayed[num] += 1

            if num <= -small[0]:
                small_size -= 1
                if num == -small[0]:
                    prune(small)
            else:
                large_size -= 1
                if large and num == large[0]:
                    prune(large)

            rebalance()

        def median():
            prune(small)
            prune(large)

            if k % 2:
                return float(-small[0])
            return (-small[0] + large[0]) / 2.0

        res = []

        for i in range(k):
            add(nums[i])

        res.append(median())

        for i in range(k, len(nums)):
            add(nums[i])
            remove(nums[i - k])
            res.append(median())

        return res
