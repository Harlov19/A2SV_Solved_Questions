class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                substr = []
                while stack:
                    val = stack.pop()
                    if val == "[":
                        break
                    substr.append(val)

                num = 0
                f = 1
                while stack and stack[-1].isdigit():
                    num = num + f*int(stack.pop())
                    f*=10

                substr = "".join(reversed(substr))
                stack.append(num*substr)
            else:
                stack.append(char)
        return "".join(stack)

                

