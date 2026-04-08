class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def possible(r):
           i = 0
           j = 0
           while i < len(houses) and j < len(heaters):
                if abs(heaters[j] - houses[i]) <=r:
                    i+=1
                else:
                    if heaters[j] - houses[i] < 0:
                        j+=1
                    else:
                        break
           return i ==len(houses)
              
        l = -1
        r = 10**9
        while l+1 < r:
            mid = l+(r-l)//2
            if possible(mid):
                r = mid
            else:
                l = mid
        return r
