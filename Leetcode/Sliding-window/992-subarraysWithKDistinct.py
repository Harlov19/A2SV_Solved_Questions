class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
          def atMostk(k):
                n = len(nums)
                count = defaultdict(int)
                res = 0
                l = 0
                for r in range(n):
                    count[nums[r]]+=1
                    while len(count) > k:
                        count[nums[l]]-=1
                        if  count[nums[l]] == 0:
                            del count[nums[l]]
                        l+=1
                    
                    res+= r-l+1
                return res
          return atMostk(k)-atMostk(k-1)
