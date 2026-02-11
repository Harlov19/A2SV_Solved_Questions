class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while(True):
            visited.add(n)
            s = 0
            while(n>0):
                digit = n%10
                n = n//10
                s+= digit*digit
            n = s
            if(n == 1): 
                return True
            if(n in visited): 
                return False
           
           