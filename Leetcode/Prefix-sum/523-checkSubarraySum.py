class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0: -1}
        ac = 0
        
        for i, num in enumerate(nums):
            ac += num
            val = ac % k
            
            if val in seen:
                if i - seen[val] >= 2:
                    return True
            else:
                seen[val] = i
        
        return False
