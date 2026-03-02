class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        res = 0
        zc = 0
        for r in range(n):
            if nums[r] == 0:
                zc+=1
            while zc>1:
                if nums[l] == 0:
                    zc-=1
                l+=1
            res = max(res,r-l+1)
        return res-1
