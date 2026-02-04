"""
Leetcode 1893
You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.

An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.
"""

class Solution:
    
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        def helper( value):
            for interval in ranges:
                if(interval[0]<=value<=interval[1]):
                    return True
               
            return False
        for num in range(left,right+1):
            included = helper(num)
            if(not included):
                return False
        return True
