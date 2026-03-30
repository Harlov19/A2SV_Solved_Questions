class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
       path = []
       res = []
       def bct(l):
        if len(path) == k:
            res.append(path.copy())
            return
        for i in range(l,n - (k-len(path))+2):
            path.append(i)
            bct(i+1)
            path.pop()
       bct(1)
       return res
