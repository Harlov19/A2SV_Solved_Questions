class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        visited = [[False]*m for _ in range(n)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(x, y, px, py, color):
            visited[x][y] = True
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                
                if grid[nx][ny] != color:
                    continue
                
                if not visited[nx][ny]:
                    if dfs(nx, ny, x, y, color):
                        return True
                else:
                    if nx != px or ny != py:
                        return True
            
            return False
        
        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True
        
        return False
