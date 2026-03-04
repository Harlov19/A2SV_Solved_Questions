for _ in range(int(input())):
    n = int(input())
    r = map(int,input().split())

    m = int(input())
    b = map(int,input().split())
    max_r = 0
    acr = 0
    for c in r:
        acr+=c
        max_r = max(max_r,acr)
    max_b = 0
    acb = 0
    for c in b:
        acb+=c
        max_b = max(max_b,acb)
    print(max_r + max_b)
