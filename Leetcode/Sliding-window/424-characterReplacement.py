class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        l = 0
        maxL = 0
        maxF = 0
        for r in range(len(s)):
             window[s[r]]+=1
             maxF = max(maxF,window[s[r]])
            
             while r-l+1-maxF > k:
                window[s[l]]-=1
                l+=1
              
             maxL = max(maxL,r-l+1)
        return maxL 
