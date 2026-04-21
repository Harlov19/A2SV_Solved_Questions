import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    l = 0
    while a[l] == b[l]:
        l += 1
    
    r = n - 1
    while a[r] == b[r]:
        r -= 1
    
    mn = min(b[l:r+1])
    mx = max(b[l:r+1])
    
    while l > 0 and a[l-1] <= mn:
        l -= 1
    
   
    while r < n - 1 and a[r+1] >= mx:
        r += 1
    
    
    print(l + 1, r + 1)
