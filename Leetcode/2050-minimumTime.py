class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in relations:
            adj[u - 1].append(v - 1)
            indegree[v - 1] += 1

        dp = [0] * n
        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                dp[i] = time[i]

        while q:
            u = q.popleft()
            for v in adj[u]:
                dp[v] = max(dp[v], dp[u] + time[v])
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return max(dp)
