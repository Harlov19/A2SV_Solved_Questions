class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ac = 0
        ans = []
        for num in nums:
            ac+=num
            ans.append(ac)
        return ans
        