from collections import defaultdict
n,k = map(int,input().split())
arr = list(map(int,input().split()))

count = defaultdict(int)
res = 0
l = 0
for r in range(n):
    count[arr[r]]+=1
    while len(count) > k:
        count[arr[l]]-= 1
        if count[arr[l]] == 0:
            del count[arr[l]]
        l+=1
   
    res+= r-l+1
print(res)
