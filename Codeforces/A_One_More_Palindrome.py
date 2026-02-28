for _ in range(int(input())):
    s = input()
    left = 0
    for right in range(1,len(s)//2):
        if(s[left] != s[right]):
            print("YES")
            break
        right+=1
        left+=1
    else:
        print("NO")
