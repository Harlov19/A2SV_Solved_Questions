class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while  target > 1:
            if maxDoubles > 0  and target%2 == 0:
                target = target//2
                maxDoubles-=1
            else:
                if maxDoubles == 0:
                    res += target - 1
                    break
                else:
                    target-=1
            res+=1
        return res 
