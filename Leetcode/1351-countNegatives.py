class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        col = len(grid[0])-1
        row = 0
        while row<len(grid) and col>=0:
            if(grid[row][col] < 0):
                count+= len(grid)-row
                col-=1
               
            else:
                row = row+1
        return count
