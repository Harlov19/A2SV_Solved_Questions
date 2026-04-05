class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        path = []
        n = len(nums)
        def bct(l):
            if len(path) >=2 :
                self.ans.append(path.copy())
            if l == n:
                return

            used = set()
            
            for i in range(l,n):
                if nums[i] in used:
                    continue
                if not path or nums[i] >= path[-1]:
                    path.append(nums[i])
                    used.add(nums[i])
                    bct(i+1)
                    path.pop()
        bct(0)
        return self.ans

