class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] =1
        ac = 0
        count = 0
        for  num in nums:
            ac+=num
            if ac-k in seen:
                count+= seen[ac-k]
            seen[ac]+=1
        return count
