class Solution:
    def romanToInt(self, s: str) -> int:
        symbole_value = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans = 0
        for i in range(len(s)-1):
            if symbole_value[s[i]] < symbole_value[s[i+1]]:
                ans-=symbole_value[s[i]]
            else:
                ans+=symbole_value[s[i]]
        ans+=symbole_value[s[-1]]
        return ans