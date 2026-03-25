class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []
        seen = set()
        
        def backtrack():
            if len(path) == len(nums):
                ans.append(path.copy())
                return 
            for num in nums:
                if num not in seen:
                    seen.add(num)
                    path.append(num)
                    
                    backtrack()
                    seen.remove(path.pop())
        backtrack()
        return ans
            