class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:

        i = 0 
        xy_count = 0
        yx_count = 0
        while i<len(s1):
            if(s1[i] == s2[i] ):
                i+=1
                continue
            elif(s1[i] == "x" and s2[i] == "y"):
                xy_count+=1
            elif(s1[i] == "y" and s2[i] == "x"):
                yx_count+=1
            i+=1
        if(xy_count + yx_count)%2 !=0:
            return -1
        if(xy_count%2 !=0):
            return xy_count//2 +  yx_count//2 +2
        else:
            return  xy_count//2 +  yx_count//2
        
       
            
