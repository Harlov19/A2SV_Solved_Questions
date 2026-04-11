import math
w,h,n = map(int,input().split())
def possible(k):
    return (k//w)*(k//h) >=n
l = 0
r = max(w,h)*n
while l+1 < r :
    mid = l+(r-l)//2
    if possible(mid):
        r = mid
    else:
        l = mid
print(r)
