class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        ac = 0
        ans = 0
        for num in nums[:n-1]:
            ac+=num
            if (ac - (total-ac))%2 == 0:
                ans+=1
        return ans
        
