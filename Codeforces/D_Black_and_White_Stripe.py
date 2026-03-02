for _ in range(int(input())):
    n,k  = map(int,input().split())
    stripe = input()
    mb = 0
    cb = 0
    for c in stripe[:k]:
        if c == "B":
            cb+=1
    mb = cb
    l = 0
    for r in range(k,n):
        if stripe[r] == "B":
            cb+=1
        if stripe[l] == "B":
            cb-=1
        l+=1
        mb = max(mb,cb)
    print(k-mb)
    
