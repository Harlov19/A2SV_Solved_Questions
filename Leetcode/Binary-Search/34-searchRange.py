class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(left,right):
            ans = -1
            while left <= right:
                mid = left+ (right-left) //2
                if nums[mid] == target:
                    ans = mid
                    right = mid-1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return ans

        def last(left,right):
            ans = -1
            while left <= right:
                mid = left+ (right-left) //2
                if nums[mid] == target:
                    ans = mid
                    left = mid+1
                elif nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            return ans
        

        return [first(0,len(nums)-1),last(0,len(nums)-1)]
                        
