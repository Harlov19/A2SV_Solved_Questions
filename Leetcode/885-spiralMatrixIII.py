class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        r,c = rStart,cStart
        size = rows*cols
        turn = 0
        steps = 1
        ans = [[rStart,cStart]]
        count = 1
        while count < size:
            for _ in range(2):
                dr,dc = directions[turn]
                for _ in range(steps):
                    r+= dr
                    c+=dc
                    if 0 <= r < rows and  0<= c < cols:
                            ans.append([r,c])
                            count+=1
                            if count == size:
                                return ans
                turn = (turn+1)%4
            steps+=1
        return ans

