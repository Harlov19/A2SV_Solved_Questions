class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def inbound(r,c):
            return 0 <=r<len(grid) and 0<=c<len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
        def dfs(r,c):
            if not inbound(r,c):
                return 1
            if grid[r][c] == 0:
                return 1
            
            visited.add((r,c))

            preimeter = 0
            for x,y in directions:
                newr,newc = r+x,c+y
                if (newr,newc) not in visited:
                    preimeter+=dfs(newr,newc)
                
            return preimeter

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:
                    return dfs(i,j)
