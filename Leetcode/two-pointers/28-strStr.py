class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        n,m = len(haystack),len(needle)
        for i in range(n):
            if(haystack[i] ==  needle[0]):
                j = 0
                while j < m  and j+i < n and needle[j] ==  haystack[j+i]:
                    j+=1
                if j == m:
                    return  i
            i+=1
        return -1
                
