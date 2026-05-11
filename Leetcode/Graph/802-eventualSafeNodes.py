class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reversedGraph = [[] for _ in range(n)]
        indegree = [0]*n
        for i in range(n):
            for j in graph[i]:
                reversedGraph[j].append(i)
                indegree[i]+=1
        q = deque([i for i in range(n) if indegree[i] == 0])
        ans = []
        while q:
            curr = q.popleft()
            ans.append(curr)
            for nei in reversedGraph[curr]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        return sorted(ans)
