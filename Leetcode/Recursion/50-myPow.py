class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1/self.pow(x,-n)
        else:
            return self.pow(x,n)
    def pow(self, x: float, n: int):
        if n == 0:
            return 1
        half = self.pow(x,n//2)  
        if n%2 == 0:
            return half*half
        else:
            return x*half*half