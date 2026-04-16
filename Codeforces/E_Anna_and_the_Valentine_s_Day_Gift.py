t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    total_digits = 0
    trailing_zeros = []
    
    for s in a:
        s = str(s)
        total_digits += len(s)
        
        z = 0
        for ch in reversed(s):
            if ch == '0':
                z += 1
            else:
                break
        
        if z > 0:
            trailing_zeros.append(z)
    
    trailing_zeros.sort(reverse=True)
    
    removed = 0
    for i in range(len(trailing_zeros)):
        if i % 2 == 0:
            removed += trailing_zeros[i]
    
    remaining = total_digits - removed
    
    if remaining >= m + 1:
        print("Sasha")
    else:
        print("Anna")
