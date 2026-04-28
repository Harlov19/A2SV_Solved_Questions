n = int(input())
pos = list(map(int,input().split()))
speeds = list(map(int,input().split()))
def good(t):
    max_l = float('-inf')
    min_r = float('inf')
    for i in range(n):
        x = pos[i]
        max_l  = max(max_l ,x- speeds[i]*t)
        min_r = min(min_r, x + speeds[i]*t)
    return max_l <= min_r
l = -1
r = 10e9 
for _ in range(70):
    m = l+(r-l)/2
    if good(m):
        r = m
    else:
        l = m
print(r)