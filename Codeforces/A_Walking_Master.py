t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())
    
    dx = c - a
    dy = d - b
    
    if dy < 0 or dy < dx:
        print(-1)
    else:
        print(2 * dy - dx)
