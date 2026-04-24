class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        prev = nums[-1]
        res = 0
        for i in range(len(nums)-2,-1,-1):
            if prev < nums[i]:
                k = math.ceil(nums[i]/prev) #split parts
                res += k-1
                prev = nums[i]//k
            else:
                prev = nums[i]
        return res

