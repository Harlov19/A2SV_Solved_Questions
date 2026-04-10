import math
n,k = map(int,input().split())
ropes = [int(input()) for _ in range(n)]

def possible(l):
    res = 0
    for rope in ropes:
        res += math.floor(rope/l)
    return res>=k
eps = 10e-6
l = 0
r = max(ropes)
m = math.ceil(math.log2((r-l)/eps))
for _ in range(100):
    mid = l+(r-l)/2
    if possible(mid):
        l = mid
    else:
        r = mid
print(l)
