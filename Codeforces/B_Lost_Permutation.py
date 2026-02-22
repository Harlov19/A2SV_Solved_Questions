t = int(input())
for _ in range(t):
    m,s = map(int,input().split())
    found_num = set(map(int,input().split()))
    max_num = max(found_num)
    
    for i in range(1,max_num):
        if(s<i or s==0):            
            break
        if i not in found_num:
            found_num.add(i)
     
            s-=i
    if s == 0:
         for i in range(1,max_num):
            if i in found_num:
                continue
            else:
                print("NO")
                break
         else:
            print("YES")
    
    else:
        curr_max = max_num+1
        while s>=curr_max:
            found_num.add( curr_max)
            s-=curr_max
            curr_max+=1

        if(s == 0):
            print("YES")
        else:
            print("NO")
   
        


