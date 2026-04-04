for _ in range(int(input())):
    n = int(input())
    s = input()
    path = []
    def bct(start):
        if start==n and len(path)>=2:
            return True
        if start==n:
            return False
        for j in range(start,n):
            cur_s = s[start:j+1]
            curr = int(cur_s)
            if not path or  int(path[-1]) < curr:
                path.append(cur_s)
                if bct(j+1):
                    return True
                path.pop()

    if bct(0):
        print("YES")
        print(len(path))
        print(*path)
    else:
        print("NO")
