class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row_n = len(img)
        col_n = len(img[0])
        ans = [[0]*col_n for _ in range(row_n)]
        for row in range(row_n):
            for col in range(col_n):
                sum = 0
                count = 0
                for new_row in range(max(0,row-1),min(row+2, row_n)):
                    for new_col in range(max(0,col-1),min(col+2,col_n)):
                        count+=1
                        sum+=img[new_row][new_col]
                ans[row][col] = sum//count
        return  ans
                    
