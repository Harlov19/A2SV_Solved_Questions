class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_ac = 1
        ans = []
        for num in nums:
            ans.append(l_ac)
            l_ac*=num

        r_ac = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=r_ac
            r_ac*=nums[i]
        return ans

        
