class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        directions = [
        (0, 1), # right
        (1, 1), # right down
        (1, 0), # down
        (1, -1), # down left
        (0, -1), # left
        (-1, -1), # left up
        (-1, 0), # up
        (-1, 1) # right, up
        ]
        n = len(grid)
        maxLocal = [[0  for _ in range(n-2)] for _ in range(n-2)]
        for row in range(1,n-1):
            for col in range(1,n-1):
                maxnum = grid[row][col]
                for dx,dy in directions:
                    new_row = row + dx
                    new_col = col + dy
                    maxnum = max(maxnum,grid[new_row][new_col])
                maxLocal[row-1][col-1] = maxnum
        return maxLocal
