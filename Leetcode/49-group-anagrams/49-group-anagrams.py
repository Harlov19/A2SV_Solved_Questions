class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for str in strs:
            sort = "".join(sorted(str))
            anagram[sort].append(str) 
        return list( anagram .values())
      
