class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def good(cap):
            dur = 1
            total = 0
            for weight in weights:
                if total + weight <= cap:
                    total += weight
                else:
                    dur += 1
                    total = weight
            return dur <= days

        l = max(weights)-1
        r = sum(weights)
        while l+1 < r:
            mid = l+(r-l)//2
            if good(mid):
                r = mid
            else:
                l = mid
        return r
