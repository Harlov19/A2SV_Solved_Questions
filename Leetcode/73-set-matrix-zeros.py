class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
         first_row = False
         first_col = False
    
         for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if(matrix[row][col] == 0):
                    matrix[row][0] = 0.5
                    matrix[0][col] = 0.5
                    if(row == 0): first_row = True
                    if(col == 0): first_col = True

         
         for row in range(len(matrix)):
            if(row == 0 and not first_row):
                continue
            if(matrix[row][0] == 0.5 ):
                for col in range(len(matrix[0])):
                    if(col == 0 and first_col):
                        continue
                    if(col == 0 and not first_col):
                        matrix[row][col] = 0
                        continue
                    if (matrix[row][col] == 0.5 and row == 0 ):
                        continue
                    matrix[row][col] = 0

         for col in range(len(matrix[0])):
             if(matrix[0][col] == 0.5):
                for row in range(len(matrix)):
                    matrix[row][col] = 0


         return matrix
