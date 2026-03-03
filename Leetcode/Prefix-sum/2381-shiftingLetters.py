class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0]*n
        for start,end,dir in shifts:
            if dir == 1:
                arr[start]+=1
                if end < n-1:
                    arr[end+1]-=1
            else:
                arr[start]-=1
                if end < n-1:
                    arr[end+1]+=1
        prefix = []
        ac = 0
        for num in arr:
            ac+=num
            prefix.append(ac)
        ans = []
        for i,char in enumerate(s):
            idx = ord(char)-ord('a')
            new_char = chr((idx + prefix[i])%26 + ord('a'))
            ans.append(new_char)
        return "".join(ans)

