t = int(input())
for _ in range(t):
    n, w = map(int, input().split())
    div = n // w
    rem = min(n % w, w - 1)
    print(div * (w - 1) + rem)
