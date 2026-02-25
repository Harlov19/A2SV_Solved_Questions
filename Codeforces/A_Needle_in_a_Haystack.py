from collections import Counter
T = int(input())
for _ in range(T):
    s = input()
    t = input()
    
    s_count = Counter(s)
    t_count = Counter(t)
    for char,count in  s_count.items():
        if (t_count[char] < count):
            print("Impossible")
            break
        else:
          t_count[char]-= count
    else:
        new_t = []
        for key ,value in t_count.items():
            new_t.extend(key*value)
        new_t.sort()
        
        ans = []
        i = 0
        j = 0
        while i <len(s) and j<len(new_t):
            if new_t[j] < s[i]:
                ans.append(new_t[j])
                j+=1
            else:
                 ans.append(s[i])
                 i+=1
        ans.extend(list(s[i:]))
        ans.extend(list(new_t[j:]))

        print("".join(ans))
                

