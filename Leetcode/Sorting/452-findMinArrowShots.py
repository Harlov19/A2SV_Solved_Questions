class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 0
        i = 0
        while i<len(points):
            if(i == len(points)-1):
                ans+=1
                break
            
            j = i+1
            interval = points[i]
            while j<len(points) and points[j][0] <= interval[1]:
                interval = [max(interval[0],points[j][0]),min(interval[1],points[j][1])]
                j+=1
               
            i = j
            ans+=1
        return ans


