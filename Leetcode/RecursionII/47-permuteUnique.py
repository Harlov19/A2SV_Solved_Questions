class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path = []
        res = []
        used = [False]*len(nums)
        def bct():
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if i> 0 and nums[i] == nums[i-1]:
                    if not used[i-1]:
                        continue
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    bct()
                    path.pop()
                    used[i] = False
                
        bct()
        return res

           
            


