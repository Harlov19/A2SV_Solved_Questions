class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid) ,len(grid[0])
        def inbound(r,c):
            return 0 <= r < m and 0 <= c< n
        q = deque()
        fresh = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        minutes = 0

        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                 
                for dx,dy in dirs:
                    nr,nc = r+dx,c+dy

                    if not inbound(nr,nc):continue
                    if grid[nr][nc] !=1:continue

                    q.append((nr,nc))
                    grid[nr][nc] = 2
                    fresh-=1
 
            minutes+=1
        if fresh > 0:
            return -1
        else:
            return minutes
