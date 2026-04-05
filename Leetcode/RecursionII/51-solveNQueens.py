class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        self.ans = []

        cols = set()
        main_diag = set()
        anti_diag = set()
        def bct(r):
            if r == n:
                self.ans.append([''.join(row) for row in board])
                return 
            for c in range(n):
                if c  in cols or (r-c) in main_diag or (r+c)  in anti_diag:
                    continue
                board[r][c] = "Q"
                cols.add(c)
                main_diag.add(r-c)
                anti_diag.add(r+c)

                bct(r+1)

                board[r][c] = '.'
                cols.remove(c)
                main_diag.remove(r-c)
                anti_diag.remove(r+c)
        bct(0)
        return self.ans
