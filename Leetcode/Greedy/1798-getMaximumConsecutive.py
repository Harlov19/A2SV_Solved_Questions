class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        miss =1 
        for coin in coins:
            if coin <=miss:
                miss+=coin
            else:
                break
        return miss
            
