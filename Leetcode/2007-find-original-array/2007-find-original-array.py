class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if(len(changed) % 2 !=0):
            return []
        counts = Counter(changed)
        original = []
        for key in sorted(counts):
            if(key == 0):
                if counts[key]%2 != 0:
                    return []
                original.extend([0]*(counts[key]//2))
                counts[key] = 0
                continue
            if(counts[2*key]<counts[key]):
                return []
            else:
               original.extend([key]*counts[key]) 
               counts[2*key]-=counts[key]
               counts[key] = 0

        return original