class Solution:
    def getAncestors(self, n, edges):
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        anc = [set() for _ in range(n)]
        q = deque(i for i in range(n) if indegree[i] == 0)

        while q:
            u = q.popleft()
            for v in adj[u]:
                anc[v].add(u)
                anc[v] |= anc[u]
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return [sorted(list(s)) for s in anc]
