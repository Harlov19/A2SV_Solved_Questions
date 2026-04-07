class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def good(k):
            tot = 0
            for pile in piles:
                tot += math.ceil(pile/k)
            return tot <= h
        l = 1
        r = sum(piles)
        ans = 0
        while l<=r:
            mid = l+(r-l)//2
            if good(mid):
                ans = mid
                r = mid-1
            else:
                l = mid + 1
        return ans
