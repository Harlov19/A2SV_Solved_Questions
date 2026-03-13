class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
      prefix = [0]
      for num in nums:
            prefix.append(prefix[-1] + num)
            
      stack = []
      maxp = 0
      nums.append(float("-inf"))
      for i in range(len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                curr = stack.pop()
                right = i
                left = stack[-1] if stack else -1
                _sum = prefix[right] - prefix[left+1]
                min_p = _sum*nums[curr]
                maxp = max(maxp,min_p)
            stack.append(i)
      return maxp%(10**9 + 7)
    
            
      
