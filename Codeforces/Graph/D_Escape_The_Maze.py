from collections import deque

for _ in range(int(input())):
    input()
    n, k = map(int, input().split())
    friends = list(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    dist_friend = [-1] * (n + 1)
    q = deque()
    
    for f in friends:
        dist_friend[f] = 0
        q.append(f)
    
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist_friend[v] == -1:
                dist_friend[v] = dist_friend[u] + 1
                q.append(v)
    
    dist_vlad = [-1] * (n + 1)
    q = deque([1])
    dist_vlad[1] = 0
    
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist_vlad[v] == -1:
                dist_vlad[v] = dist_vlad[u] + 1
                q.append(v)
    
    can_escape = False
    
    for i in range(2, n + 1):
        if len(adj[i]) == 1:
            if dist_vlad[i] < dist_friend[i]:
                can_escape = True
                break
    
    print("YES" if can_escape else "NO")
