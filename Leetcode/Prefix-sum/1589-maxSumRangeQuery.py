class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0]*(n+1)
        for start,end in requests:
            freq[start]+=1
            freq[end+1]-=1
        ac = 0
        f_prefix = []
        for i in range(n):
            ac+= freq[i]
            f_prefix.append(ac)
        f_prefix.sort(reverse = True)
        nums.sort(reverse = True)
       
        ans = 0
        for i in range(n):
            ans+= f_prefix[i]*nums[i]
        
        return ans%(10**9 + 7)


        



        
