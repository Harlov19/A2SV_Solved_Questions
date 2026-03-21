class Solution:
    def lastRemaining(self, n: int) -> int:
        def helper(head, step, n, left):
            if n == 1:
                return head
            if left or n % 2 == 1:
                head += step
            return helper(head, step * 2, n // 2, not left)
        
        return helper(1, 1, n, True)
