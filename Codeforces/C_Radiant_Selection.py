import math
for _ in range(int(input())):
    k = int(input())
    left = k
    right = 2*10**18
    ans = -1
    while left<=right:
        mid = left + (right-left)//2
        if mid - int(math.isqrt(mid)) >= k:
            ans = mid
            right = mid-1

        else:
            left = mid + 1
    print(ans)
