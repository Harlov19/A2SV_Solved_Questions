class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_min = [min(row) for row in matrix]
        col_max = [max(col) for col in zip(*matrix)]


        return [
            matrix[i][j]
            for i in range(len(matrix))
            for j in range(len(matrix[0]))
            if  matrix[i][j] == row_min[i] and  matrix[i][j] == col_max[j]
        ]
