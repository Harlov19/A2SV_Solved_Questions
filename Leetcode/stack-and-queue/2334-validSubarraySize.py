class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        stack = []
        nums.append(float("-inf"))
        for i,num in enumerate(nums):
           while stack and num < nums[stack[-1]]:
                curr = stack.pop()
                right = i
                left = stack[-1] if stack else -1

                k = right - left-1
                if nums[curr]*k > threshold:
                    return k
           stack.append(i)
         
        return -1
