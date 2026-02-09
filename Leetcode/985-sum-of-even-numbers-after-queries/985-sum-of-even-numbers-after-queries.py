class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        even_sum = 0
        for num in nums:
            if(num%2 == 0):
                even_sum+=num
        ans = []
        for val,index in queries:
            old = nums[index] 
            if(old%2==0):
                even_sum-=old
            new_val =  nums[index]+val
            nums[index] = new_val
            if(new_val%2==0):
                even_sum+= new_val
            ans.append(even_sum)
        return  ans