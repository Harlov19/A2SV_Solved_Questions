class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        def inbound(r,c):
            return 0 <= r < n and 0 <= c < n
        dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
        q = deque([(0,0)])
        visited = set([(0,0)])

        dist = 1
        
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                
                if (r,c) == (n-1,n-1):
                    return dist
                for dx,dy in dirs:
                    nr,nc = r+dx,c+dy
                    if inbound(nr,nc) and grid[nr][nc] == 0 and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))
            
            dist+=1
        return  -1
