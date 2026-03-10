class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        stack = []
        next = defaultdict(lambda: -1)
        for num in nums2:
           while stack and stack[-1] < num:
                next[stack[-1]] = num
                stack.pop()
           stack.append(num)
           
        return [next[num] for num in nums1 ]

