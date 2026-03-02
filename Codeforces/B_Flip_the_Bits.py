for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    prefix = [] #0 balance 1 unbalanced
    z = 0 # no of zeros
    for i in range(n):
        if a[i] == "0":
            z+=1
        if z == i+1-z:
            prefix.append(0)
        else:
            prefix.append(1)
    flipped = 0
    for i in range(n-1,-1,-1):
        curr = a[i] if flipped == 0 else ("1" if a[i] == '0' else "0")
        if  curr != b[i]:
            if prefix[i] != 0:
                print("NO")
                break
            else:
               flipped = abs(flipped-1) 
    else:
        print("YES")
