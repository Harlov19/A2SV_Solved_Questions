class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bf = 0
        bt = 0
        for bill in bills:
            if bill == 5:
                bf+=1
                continue
            elif bill == 10:
                if bf > 0:
                    bf-=1
                    bt+=1
                else:
                    return False
            else:
                if bt > 0 and bf > 0:
                    bf-=1
                    bt-=1
                elif bf>2 :
                    bf-=3
                else:
                    return False
                
        return True
