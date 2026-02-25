class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = {}
        for i,char in enumerate(s):
           last_seen[char] = i

        ans = []
        i = 0
        while i < len(s):
            le = 0
            max_d = last_seen[s[i]]

            while i <= max_d:
                max_d = max(max_d,last_seen[s[i]])
                le+=1
                i+=1
                
            ans.append(le)
        return ans
