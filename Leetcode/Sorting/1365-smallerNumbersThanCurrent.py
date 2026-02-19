class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = [0]*501
        for num in nums:
            counts[num]+=1
        smaller = 0
        mapping= {}
        for i in range(501):
            mapping[i] = smaller
            smaller+=counts[i]
        ans = []
        for num in nums:
            ans.append(mapping[num])
        return  ans
