t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    s = input().strip()
    w = input().strip()
    
    target = sum(ord(c) - ord('a') for c in w)
    
    window = sum(ord(s[i]) - ord('a') for i in range(m))
    
    if window == target:
        print("YES")
        continue
    
    found = False
    
    for i in range(m, n):
        window += ord(s[i]) - ord('a')
        window -= ord(s[i - m]) - ord('a')
        
        if window == target:
            found = True
            break
    
    print("YES" if found else "NO")
