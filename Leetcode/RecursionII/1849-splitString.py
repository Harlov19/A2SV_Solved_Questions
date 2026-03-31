class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        split = []
        def bct(l):
            if l == n:
                return len(split) >=2
                    
            
            for i in range(l,n):
                if not split or  int(split[-1])- int(s[l:i+1]) == 1:
                    split.append(s[l:i+1])
                    if bct(i+1):
                        return True
                    split.pop()
        
            return False
        return bct(0)
