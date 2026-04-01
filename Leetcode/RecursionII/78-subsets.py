class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        sub = []
        n = len(nums)
        def bct(l):
            if l >= n:
                return
            for i in range(l,n):
                sub.append(nums[i])
                ans.append(sub.copy())
                bct(i+1)
                sub.pop()
             
        bct(0)
        return ans
