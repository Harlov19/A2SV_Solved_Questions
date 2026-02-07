"""
Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].
"""

class Solution:
    def isSubset(self, a, b):
        def counter(arr):
            count = {}
            for num in arr:
                count[num] = count.get(num, 0) + 1
            return count

        count_a = counter(a)
        for num in b:
            if (num not in count_a or count_a[num] < 1):
                return False
            count_a[num] -= 1
        return True

           
    