class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flips = 0
        dq = deque()
        for i in range(n):
            while dq and dq[0] + k <=i:
                dq.popleft()
            effective = nums[i]^(len(dq)%2)
            if  effective == 0:
                if i+k > n:
                    return -1
                flips+=1
                dq.append(i)
        return flips

