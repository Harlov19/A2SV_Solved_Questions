class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        n = len(nums)
        return [num for  num in counts if counts[num]> floor(n/3)]
        