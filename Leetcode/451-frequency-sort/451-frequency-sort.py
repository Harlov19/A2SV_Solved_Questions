class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        ans = []
        for char,freq in sorted(counts.items(),key=lambda x: -x[1]):
            ans.extend([char[0]]*freq)
        return "".join(ans)