t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    a.sort()
    
    for i in range(n - 1, 0, -2):
        diff = a[i] - a[i - 1]
        take = min(diff, k)
        a[i - 1] += take
        k -= take
    
    a.sort(reverse=True)
    
    A = 0  
    B = 0  
    
    for i in range(n):
        if i % 2 == 0:
            A += a[i]
        else:
            B += a[i]
    
    print(A - B)
