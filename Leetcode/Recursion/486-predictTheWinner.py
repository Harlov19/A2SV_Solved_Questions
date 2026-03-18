class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        l = 0
        r = len(nums)-1
        def dp(l,r):
            if l == r:
                return nums[l]
            left = nums[l]-dp(l+1,r)
            right = nums[r] - dp(l,r-1)
            return max(left,right)
        return dp(l,r) >= 0
