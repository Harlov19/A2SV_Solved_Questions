class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        size = min(m,n)

        for k  in range(size,0,-1):
            for i in range(n-k+1):
                for j in range(m-k+1):
                    if self.is_magic_square(grid,i,j,k):
                        return k
    def is_magic_square(self, grid, x, y, k):
        diag_sum = 0
        anti_diag_sum = 0
        for i in range (k):
            diag_sum+=grid[x+i][y+i]
            anti_diag_sum+=grid[x+i][y+k-i-1]
        if diag_sum != anti_diag_sum:
            return False
        

        row_sum = 0
        for i in range(k):
            row_sum = sum(grid[x+i][y:y+k])
            if(row_sum !=diag_sum):
                return False
            col_sum = sum(grid[x+j][y+i] for j in range(k))
            if(col_sum !=diag_sum):
                return False
        return True

    
