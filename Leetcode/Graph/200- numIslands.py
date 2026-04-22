class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def inbound(r,c):
            return 0 <=r<len(grid) and 0<=c<len(grid[0]) 
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        def dfs(r,c):
            visited.add((r,c))
            for x,y in directions:
                newr,newc = r+x,c+y
    
                if inbound(newr,newc) and grid[newr][newc] == '1' and (newr,newc) not in visited:
                    dfs(newr,newc)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                    if (i,j) not in visited and grid[i][j] == '1':
                        dfs(i,j)
                        count+=1
        return count
