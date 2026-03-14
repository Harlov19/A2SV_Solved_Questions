class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        prev = nums[0]

        for num in nums[1:]:
            while stack and num >= stack[-1][1]:
                stack.pop()

            if stack and num > stack[-1][0]:
                return True

            stack.append((prev, num))
            prev = min(prev, num)

        return False
