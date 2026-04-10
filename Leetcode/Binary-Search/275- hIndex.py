class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def good(h):
            p = 0
            for cite in citations:
                if cite>=h:
                    p+=1
            return p>=h
        l = 0
        r = max(citations) + 1
        while l+1 < r:
            m = l+(r-l)//2
            if good(m):
                l = m
            else:
                r = m
        return l
