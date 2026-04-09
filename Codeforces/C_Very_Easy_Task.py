n,x,y = map(int,input().split())

if n == 1:
    print(min(x,y))
else:
    intial = min(x,y)
    remaining = n-1
    def good(t):
        return (t//x + t//y) >= remaining
    l = 0
    r = n*(max(x,y)) 

    while l+1 < r:
        m = l+(r-l)//2
        if good(m):
            r = m
        else:
            l = m
    print(r + intial)
