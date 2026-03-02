from collections import defaultdict
n,k = map(int,input().split())
a = list(map(int,input().split()))

counts = defaultdict(int)
l = 0
maxL = 0
ans = [0,0]
for r in range(n):
    counts[a[r]]+=1
    while len(counts) > k:
        counts[a[l]]-=1
        if counts[a[l]] == 0:
            del counts[a[l]]
        l+=1
    if r-l+1 >maxL:
        maxL = r-l+1
        ans[0],ans[1] = l+1,r+1
print(*ans)



