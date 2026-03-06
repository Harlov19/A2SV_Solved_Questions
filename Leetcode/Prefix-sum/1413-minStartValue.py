class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ac = 0
        _min = float("inf")
        for num in nums:
            ac += num
            _min = min(_min, ac)
        return max(1, 1 - _min)
