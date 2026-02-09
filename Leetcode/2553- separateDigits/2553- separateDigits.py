class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        def getDigit(num):
            return [ int(digit) for digit in str(num)]
        ans = []
        for num in nums:
            ans.extend(getDigit(num))
        return ans
