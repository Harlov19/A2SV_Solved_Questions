t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input()

    first_zero = False

    for i in range(n):
        if k == 0:
            break
        if s[i] == "L":
            x -= 1
        else:
            x += 1
        k -= 1
        if x == 0:
            first_zero = True
            break

    if not first_zero:
        print(0)
        continue

    ans = 1
    x = 0
    cycle_len = 0
    second_zero = False

    for i in range(n):
        if s[i] == "L":
            x -= 1
        else:
            x += 1
        cycle_len += 1
        if x == 0:
            second_zero = True
            break

    if second_zero and k > 0:
        ans += k // cycle_len

    print(ans)
