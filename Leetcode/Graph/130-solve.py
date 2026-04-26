class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board),len(board[0])
        dirs = [(0,-1), (0,1), (1,0), (-1,0)]

        def dfs(r,c):
            board[r][c] = 'T'

            for dx,dy in dirs:
                newr,newc = r+dx,c+dy
                if 0 <= newr < m and 0 <= newc < n and board[newr][newc] == 'O':
                    dfs(newr,newc)
                
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][n-1] == 'O':
                dfs(i,n-1)
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[m-1][j] == 'O':
                dfs(m-1,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
      
