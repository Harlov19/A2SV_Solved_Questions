"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       shortest = min(strs,key=len)
       isEqual = True
       count = 0
       for i in range(len(shortest)):
            if(not isEqual):
                break
            for word in strs:
                if(shortest[i] != word[i]):
                    isEqual = False
                    break
                           
            if(isEqual):
                count+=1
       return shortest[:count]


