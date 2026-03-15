from collections import deque

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        flips = 0
        dq = deque()
        for i in range(n):
            while dq and dq[0] + 3 <=i:
                dq.popleft()
            effective = nums[i]^(len(dq)%2)
            if  effective == 0:
                if i+3 > n:
                    return -1
                flips+=1
                dq.append(i)
        return flips
