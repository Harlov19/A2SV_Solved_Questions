class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        diag_elem = defaultdict(list)
        ans = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diag_elem[i+j].append(mat[i][j])
        up = True
        for key in sorted(diag_elem):
            value = diag_elem[key]
            if(up):
                ans.extend(list(value)[::-1])
            else:
                ans.extend(list(value))
            up = not up
        return ans
