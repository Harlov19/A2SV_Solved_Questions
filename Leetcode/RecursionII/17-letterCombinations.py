class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'
                }
        ans = [] 
        path = []
        def backtrack(i):
            if len(path) == len(digits):
                copy = "".join(path)
                ans.append(copy)
            if i == len(digits):
                return
            for char in digitMap[digits[i]]:
                path.append(char)
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return ans
