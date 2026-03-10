class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        next = [0]*n
        stack = []

        for i,temp in enumerate(temperatures):
            count = 0
            while stack and temperatures[stack[-1]] < temp:
                next[stack[-1]] = i-stack[-1]
                stack.pop()
            stack.append(i)
        return next
