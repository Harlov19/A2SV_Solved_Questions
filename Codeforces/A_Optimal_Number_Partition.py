n = int(input())
a = list(map(int, input().split()))

a.sort()

ans = 0
l, r = 0, n - 1

while l < r:
    s = a[l] + a[r]
    ans += s * s
    l += 1
    r -= 1

print(ans)
