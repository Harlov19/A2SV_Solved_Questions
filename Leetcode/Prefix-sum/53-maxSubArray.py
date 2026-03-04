class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        mins = 0
        ac = 0
        for num in nums:
            ac+=num
            res = max(res,ac-mins)
            mins = min(mins,ac)
        return res
        
