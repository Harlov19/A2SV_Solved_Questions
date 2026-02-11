from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    left = 0
   
    minLen = float("inf")
    
    for i in range(n-1):
        counts = defaultdict(int)
        counts[s[i]]+=1
        for j in range(i+1, min(n,i+7)):
            counts[s[j]]+=1
            if(counts["a"]>counts["b"] and counts["a"]>counts["c"]):
                minLen = min(minLen,j-i+1) 
                break
    print(minLen) if minLen != float("inf") else print(-1)



        
            
