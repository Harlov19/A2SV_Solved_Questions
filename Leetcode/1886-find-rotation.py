class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if(mat == target):
            return True
        for i in range(3):
            mat = self.rotateMatrix(mat)
            if(mat == target):
                return True
        return False
            
    
    def rotateMatrix(self,matrix):
            transposed = []
            for row in zip(*matrix):
                transposed.append(list(row))
        
            n ,m= len(transposed), len(transposed[0])
            for i in range(n):
                for j in range(m//2):
                    transposed[i][j],transposed[i][m-1-j] = transposed[i][m-1-j],transposed[i][j] 
            return  transposed

