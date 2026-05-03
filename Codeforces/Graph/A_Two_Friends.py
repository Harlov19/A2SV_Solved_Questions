for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    
    found = False
    
    for i in range(n):
        if p[p[i] - 1] == i + 1:
            found = True
            break
    
    print(2 if found else 3)
