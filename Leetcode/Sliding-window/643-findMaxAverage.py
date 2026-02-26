class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        maxSum = window_sum

        for i in range(k,len(nums)):
           window_sum += nums[i] 
           window_sum-= nums[i-k]
           
           maxSum = max( maxSum ,window_sum)
        return maxSum/k