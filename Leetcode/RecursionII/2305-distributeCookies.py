class Solution:   
    def distributeCookies(self, cookies: List[int], k: int) -> int:
       share = [0]*k
       self.minunf = float('inf')
       def bct(l):
            if  l>=len(cookies):
                self.minunf = min(self.minunf,max(share))
                return
            for i in range(k):
                if share[i] + cookies[l] <  self.minunf:
                    share[i]+=cookies[l]
                    bct(l+1)
                    share[i]-=cookies[l]
       bct(0)
       return self.minunf
        
