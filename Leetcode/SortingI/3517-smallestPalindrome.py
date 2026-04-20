class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if(len(s)==1):
            return s
        f = [0]*26 
        half = len(s)//2
        for c in s[:half]: f[ord(c)-97]+=1
        l = []
        for i in range(26):
            l.extend([chr(i+97)]*f[i])
        l = "".join(l)
        if(len(s)%2 == 0):
            return l+l[::-1]
        else:
            return l+s[half]+l[::-1]

