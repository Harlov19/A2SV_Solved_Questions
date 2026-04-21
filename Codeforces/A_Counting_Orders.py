import sys
input = sys.stdin.readline

MOD = 10**9 + 7

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    
    ans = 1
    j = n - 1
    
    for i in range(n - 1, -1, -1):
        while j >= 0 and a[j] > b[i]:
            j -= 1
        
        good = n - (j + 1)  
        used = (n - 1 - i)  
        
        choices = good - used
        
        if choices <= 0:
            ans = 0
            break
        
        ans = (ans * choices) % MOD
    
    print(ans)
