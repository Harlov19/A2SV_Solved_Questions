class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(bombs)):
            xi,yi,ri = bombs[i]
            for j in range(len(bombs)):
                if i == j: continue
                xj,yj,rj = bombs[j]

                dist = (yj-yi)**2 + (xj-xi)**2
                if dist <= ri * ri:
                    graph[i].append(j)
                    
        def dfs(node,visited):
            reach = 1
            visited.add(node)
            for nei in graph[node]:
                if nei in visited:continue
                reach += dfs(nei,visited)
            return reach
        maxNum = 0
        for i in range(len(bombs)):
            maxNum = max(maxNum,dfs(i,set()))
            
        return maxNum


