class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        ans = []
        for char in order:
            ans.append(char*counts[char])
            del counts[char]
        for key,value in  counts.items():
                ans.append(key*value)
        return "".join(ans)
