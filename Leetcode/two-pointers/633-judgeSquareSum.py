class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = math.isqrt(c)
        while left<=right:
            square = left*left + right*right
            if square == c:
                return True
            if(square<c):
                left+=1
            else:
                right-=1
        return False
        
