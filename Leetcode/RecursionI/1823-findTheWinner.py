class Solution(object):
    def findTheWinner(self, n, k):
        lis =  [i for i in range(1,n+1)]

        def helper(curr):
            if len(lis) == 1:
                return lis[0]
            curr = (curr +k -1)%len(lis)
            lis.pop(curr)
            return helper(curr)
            
        return helper(0)


        
