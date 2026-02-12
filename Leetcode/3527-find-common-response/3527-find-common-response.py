class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        counts = defaultdict(int)
        for response in responses:
            words = set(response)
            for word in words:
                counts[word]+=1
        maxCount = max(counts.values())
        for key in sorted(counts):
            if(counts[key] == maxCount):
                return key
