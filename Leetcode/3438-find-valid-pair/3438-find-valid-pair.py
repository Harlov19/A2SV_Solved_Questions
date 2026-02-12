class Solution:
    def findValidPair(self, s: str) -> str:
        counts = Counter(s)
        for i in range(len(s)-1):
            if(s[i] != s[i+1] and (int(s[i])==counts[s[i]] and int(s[i+1])==counts[s[i+1]])):
                return s[i:i+2]
            
        return ""