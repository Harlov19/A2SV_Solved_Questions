class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        
        for i, citation in enumerate(citations,1):
            if citation >= i:
                h = i
            else:
                break
                
        return h
