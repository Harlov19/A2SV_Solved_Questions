class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set([source])
        
        stack = [source]
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for nei in graph[node]:
                if nei not in visited:
                    stack.append(nei)
                    visited.add(nei)

        return False
