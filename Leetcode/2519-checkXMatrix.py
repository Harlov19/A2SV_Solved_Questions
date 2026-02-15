class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n,m = len(grid),len(grid[0])
        isXMatrix = True
        for i in range(n):
            for j in range(m):
                if (i == j or j == n-1-i):
                    if(grid[i][j] == 0):
                        isXMatrix = False
                        break
                else:
                    if(grid[i][j] != 0):
                        isXMatrix = False
                        break
        return isXMatrix

