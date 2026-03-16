t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    mx = a[-1]  
    ans = 0

    for k in range(2, n):
        z = a[k]
        limit = max(z, mx - z) 
        i, j = 0, k - 1 
        while i < j:
            if a[i] + a[j] > limit:
                ans += j - i
                j -= 1
            else:
                i += 1

    print(ans)
