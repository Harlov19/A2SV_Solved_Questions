class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        commons = counts.most_common(k)
        return [x[0] for x in   commons]