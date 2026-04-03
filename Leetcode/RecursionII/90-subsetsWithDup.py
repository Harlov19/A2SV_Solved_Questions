class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def backtrack(start,subset):
            if start == len(nums):
                ans.append(subset.copy())
                return
            subset.append(nums[start])
            backtrack(start+1,subset)
            subset.pop()
            while start +1 < len(nums) and nums[start] == nums[start + 1]:
                start+=1
            backtrack(start+1,subset)
        
        backtrack(0,[])
        return ans
