for _ in range(int(input())):
    s = input()
    seen = set()
    res = []
    i = 0
    while i <len(s):
        j = i
        count = 0
        while j < len(s) and s[i] == s[j]:
            j+=1
            count+=1
        if(count%2 == 1 and s[i] not in seen):
            res.append(s[i])
            seen.add(s[i])
        i = j 
        
    print("".join(sorted(res)))

