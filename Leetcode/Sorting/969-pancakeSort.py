class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        pos = len(arr)-1
        target = pos+1
        ans = []
        while pos>0:
           idx = arr.index(target)
           if(idx == 0):
               self.reverse(pos,arr)
               ans.append(pos+1)
               pos-=1
               target = pos+1
           elif(idx == pos):
               pos-=1
               target = pos+1
               continue
           else:
              self.reverse(idx,arr) 
              ans.append(idx+1)
           
                
        return ans 


    def reverse(self,right,arr):
        left = 0
        while left<right:
            arr[left],arr[right] = arr[right],arr[left]
            left+=1
            right-=1
