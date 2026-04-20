class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        share = len(piles)//3
        ans = 0
        pos = 1
        for i in range(share):
            ans+=piles[pos]
            pos+=2

        return ans
