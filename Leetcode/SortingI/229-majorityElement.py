class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        k = n // 3
        nums.sort()
        ans = []
        i = 0

        while i < n:
            count = 1
            j = i
            while j + 1 < n and nums[j+1] == nums[j]:
                count += 1
                j += 1

            if count > k:
                ans.append(nums[i])

            i = j + 1  

        return ans
