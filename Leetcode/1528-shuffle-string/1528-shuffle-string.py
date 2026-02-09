class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [0 for i in range(len(s))]
        for i,char in enumerate(s):
            new_index = indices[i]
            ans[new_index] = char
        return "".join(ans)

