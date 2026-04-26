class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [(0,-1), (0,1), (1,0), (-1,0)]
        m,n = len(heights),len(heights[0])
        
        def dfs(r,c,ocean):
            ocean.add((r,c))
            
            for dx,dy in dirs:
                newr,newc = r+dx,c+dy
                if (
                0 <= newr < m and 0 <= newc < n and 
                (newr,newc) not in ocean and 
                heights[newr][newc] >=heights[r][c]):
                    dfs(newr,newc,ocean)
        
        pacific = set()
        for i in range(n):
            dfs(0,i,pacific)
        for j in range(m):
            dfs(j,0,pacific)
        
        atlantic = set()
        for i in range(n):
            dfs(m-1,i,atlantic)
        for j in range(m):
            dfs(j,n-1,atlantic)

        return list(pacific & atlantic)




