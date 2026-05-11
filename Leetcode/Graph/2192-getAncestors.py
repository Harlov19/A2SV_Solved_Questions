class Solution:
    def getAncestors(self, n, edges):
       graph = defaultdict(list)
       indegree = [0]*n
       for u,v in edges:
            graph[u].append(v)
            indegree[v]+=1

       q = deque([i  for i in range(n) if indegree[i] == 0])
       ans = [set() for _ in range(n)]

       while q:
            curr = q.popleft()
            for nei in graph[curr]:
                ans[nei].add(curr)
                ans[nei] |= ans[curr]
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
       
       return [sorted(anscestors) for anscestors in ans]
                

        
