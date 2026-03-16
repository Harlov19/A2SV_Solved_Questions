class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(float("-inf"))
        maxArea = 0
        stack = []
        for i,height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                curr = stack.pop()
                l = stack[-1] if stack else -1
                r = i
                area = heights[curr]*(r-l-1)
                maxArea = max(maxArea, area)
            stack.append(i)
        return maxArea
