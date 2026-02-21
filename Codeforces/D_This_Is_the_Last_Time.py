t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        li,ri,reali = map(int,input().split())
        arr.append((li,ri,reali))
    curr = k
    arr.sort()
    for li,ri,reali in arr:
        if li>curr:
            print(curr)
            break
        if li<=curr<=ri:
            curr = max(curr,reali)
    else:
        print(curr)
    
