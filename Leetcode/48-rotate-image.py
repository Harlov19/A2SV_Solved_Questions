class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for row in range(len(matrix)):
            for col in range(row+1,len(matrix[0])):
                matrix[row][col],matrix[col][row] = matrix[col][row], matrix[row][col]
        for i in range(len(matrix)):
            matrix[i].reverse()
        
     
