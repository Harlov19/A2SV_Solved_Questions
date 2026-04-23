class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        colors = defaultdict(int) # 0 black # 1 white
       
        def dfs(node,color):
            if node in colors:
                return colors[node] == color
            colors[node] = color
            
            for nei in graph[node]:
                if not dfs(nei,not color):
                    return False

            return True

        for i in range(len(graph)):
            if i not in colors:
                if not dfs(i,0):
                    return False
        return True
