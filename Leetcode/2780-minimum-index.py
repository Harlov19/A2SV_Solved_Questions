class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count_nums = Counter(nums)
        dominat = count_nums.most_common(1)[0][0]
        f = count_nums.most_common(1)[0][1]
        
        f1 = 0
        n = len(nums)
        for i in range(len(nums)):
            l1 = (i+1)//2
            l2 = (n-i-1)//2
            if(nums[i] == dominat):
                f1+=1
            f2 = f-f1
            if(f1 > l1 and f2> l2):
                return i
        return -1
        
