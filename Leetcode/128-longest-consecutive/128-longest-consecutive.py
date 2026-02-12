class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        ans = 0
        for elm in elements:
           
            if elm - 1 not in elements:
                curr = 1
                while elm + curr in elements:
                    curr += 1
                ans = max(ans, curr)

        return ans