class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        res = 0
        ac = 0
        for num in nums:
            ac+=num
            if ac-goal in seen:
                res+=seen[ac-goal]
            seen[ac]+=1
        return res
