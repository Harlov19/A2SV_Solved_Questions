class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []

        def dfs(path):
            if len(res) >= k:
                return
            
            if len(path) == n:
                res.append("".join(path))
                return
            
            for c in "abc":
                if path and path[-1] == c:
                    continue
                path.append(c)
                dfs(path)
                path.pop()

        dfs([])
        return res[k-1] if k <= len(res) else ""
