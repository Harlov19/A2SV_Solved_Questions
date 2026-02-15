class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        specialPos = 0
        row_sum = {}
        for  row in range(len(mat)):
            row_sum[row] = sum(mat[row])
        col_sum = {}
        for i, col in enumerate(zip(*mat)):
            col_sum[i] = sum(col)

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if(
                    mat[row][col] == 1 and 
                    row_sum[row] == 1 and  
                    col_sum[col] == 1):
                    
                    specialPos+=1
        return specialPos
