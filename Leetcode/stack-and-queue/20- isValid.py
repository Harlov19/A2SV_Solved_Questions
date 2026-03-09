class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if pairs[top] != char:
                    return False
                else:
                    stack.pop()
         
        if stack:
            return False
        return True
