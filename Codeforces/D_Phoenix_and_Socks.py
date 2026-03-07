for _ in range(int(input())):
    n, l, r = map(int, input().split())
    c = list(map(int, input().split()))
    
    lcnt = [0] * (n + 1)
    rcnt = [0] * (n + 1)
    
    for i in range(n):
        if i < l:
            lcnt[c[i]] += 1
        else:
            rcnt[c[i]] += 1
    
    for i in range(1, n + 1):
        m = min(lcnt[i], rcnt[i])
        lcnt[i] -= m
        rcnt[i] -= m
        l -= m
        r -= m
    
    if l < r:
        l, r = r, l
        lcnt, rcnt = rcnt, lcnt
    
    ans = 0
    for i in range(1, n + 1):
        extra = l - r
        p = lcnt[i] // 2
        t = min(p * 2, extra)
        ans += t // 2
        l -= t
    
    ans += (l - r) // 2 + (l + r) // 2
    print(ans)
