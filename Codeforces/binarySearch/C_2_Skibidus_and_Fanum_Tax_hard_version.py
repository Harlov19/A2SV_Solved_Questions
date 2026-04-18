from bisect import bisect_left
for _ in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    b.sort()
    
    prev = float('-inf')
    for i in range(n):
        low = bisect_left(b,prev + a[i])
        best = float('inf')
        if a[i]>=prev:
            best = a[i]
        if low < m:
            best = min(best,b[low]-a[i])
        if best == float('inf'):
            print("NO")
            break
        a[i] = best
        prev = a[i]
    else:
        print("YES")
