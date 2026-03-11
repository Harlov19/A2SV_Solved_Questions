class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        _max = deque()
        for i in range(k):
            while _max and nums[_max[-1]] <= nums[i]:
                _max.pop()
            _max.append(i)
        ans.append(nums[_max[0]])

        for right in range(k,len(nums)):
            while _max and nums[_max[-1]] <= nums[right]:
                _max.pop()
            _max.append(right)

            if _max[0] < right-k+1:
                _max.popleft()

            ans.append(nums[_max[0]])
        return ans
        
