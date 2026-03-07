class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        size = rows*cols
        turn = 0
        x = 1
        y = 1
        ans = [[rStart,cStart]]
        count = 1
        while count < size:
            if turn == 0:#right
                for _ in range(x):
                    cStart+=1
                    if 0 <= rStart < rows and  0<=cStart < cols:
                        ans.append([rStart,cStart])
                        count+=1
                        if count == size:
                            return ans
                x+=1
            elif turn == 1:#down
                for _ in range(y):
                    rStart+=1
                    if 0 <= rStart < rows and  0<=cStart < cols:
                        ans.append([rStart,cStart])
                        count+=1
                        if count == size:
                            return ans
                y+=1
            elif turn == 2: #left
                for _ in range(x):
                    cStart-=1
                    if 0 <= rStart < rows and  0<=cStart < cols:
                        ans.append([rStart,cStart])
                        count+=1
                        if count == size:
                            return ans
                x+=1
            else: #up
               for _ in range(y):
                    rStart-=1
                    if 0 <= rStart < rows and  0<=cStart < cols:
                            ans.append([rStart,cStart])
                            count+=1
                            if count == size:
                                return ans
               y+=1 
            
            turn = (turn+1)%4
        return ans

