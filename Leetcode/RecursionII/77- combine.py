class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start: int):
            if len(path) == k:
                res.append(path.copy())
                return

            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)
        return res
