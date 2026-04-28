import sys
sys.setrecursionlimit(10**7)
n = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

ax -= 1; ay -= 1
bx -= 1; by -= 1
cx -= 1; cy -= 1

def isIncheck(x, y):
    return (
        x == ax or
        y == ay or
        (x - y) == (ax - ay) or
        (x + y) == (ax + ay)
    )

def inBound(x, y):
    return 0 <= x < n and 0 <= y < n

directions = [
    (-1,0),(1,0),(0,-1),(0,1),
    (-1,-1),(-1,1),(1,-1),(1,1)
]

visited = set()

def dfs(x, y):
    if (x, y) == (cx, cy):
        return True

    visited.add((x, y))

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
    
        if inBound(nx, ny) and (nx, ny) not in visited and not isIncheck(nx, ny):
            if dfs(nx, ny):
                return True

    return False





print("YES" if dfs(bx,by) else "NO")
