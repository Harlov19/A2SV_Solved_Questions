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
        candidates = [digitMap[digit] for digit in digits]
        n = len(candidates)
        ans = [] 
        path = []
        def backtrack(start):
            if len(path) == len(digits):
                copy = "".join(path)
                ans.append(copy)
            if start == n:
                return
            for char in candidates[start]:
                path.append(char)
                backtrack(start+1)
                path.pop()
        backtrack(0)
        return ans
