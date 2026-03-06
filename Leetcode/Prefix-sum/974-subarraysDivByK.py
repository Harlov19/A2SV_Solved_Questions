class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        ac = 0
        res = 0
        for num in nums:
            ac+=num
            mod = ac%k
            if mod in seen:
                res+= seen[mod]
            seen[mod]+=1
        return res
