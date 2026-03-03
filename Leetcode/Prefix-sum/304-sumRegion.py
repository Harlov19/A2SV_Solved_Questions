class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        row = len(matrix)
        col = len(matrix[0])
        prefix = [[0]*(col+1) for _ in range(row+1)]

        for i in range(1,row+1):
            for j in range(1,col+1):
                top_val =  prefix[i-1][j]
                left_val = prefix[i][j-1] 
                topleft_val = prefix[i-1][j-1] 
                val = matrix[i-1][j-1]
                prefix[i][j] = top_val +   left_val - topleft_val + val

        self.prefix = prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 +=1
        col1 +=1
        row2 +=1
        col2 +=1

        ans = self.prefix[row2][col2] - self.prefix[row2][col1 - 1] - self.prefix[row1 - 1][col2] + self.prefix[row1 - 1][col1 - 1]

        return ans
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
