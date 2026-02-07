class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if nums[abs(num)-1] <0:
                ans.append(abs(num))

            index = abs(num)-1
            nums[index] = -nums[index]
        return ans
