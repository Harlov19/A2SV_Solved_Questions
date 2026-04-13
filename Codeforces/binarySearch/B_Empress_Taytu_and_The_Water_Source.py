t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    if sum(a) > k:
        print(-1)
        continue
    
    def possible(s):
        total = 0
        for i in range(n):
            trips = (d[i] + s - 1) // s
            total += trips * a[i]
            if total > k:
                return False
        return True
    
    left, right = 1, max(d)
    ans = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if possible(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    
    print(ans)
