class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        k = 0
        for num in nums:
            if num == 1:
                k+=1
        c = 0
        for num in nums[:k]:
            if num == 1:
                c+=1
        mc = c
        l = 0
        for r in range(k,2*n):
            if nums[r%n] == 1:
                c+=1
            if nums[l%n] == 1:
                c-=1
            l+=1
            mc = max(mc,c)
        return k-mc
        
