n,m = map(int,input().split())
diff = []
a_sum = 0
for _ in range(n):
    ai,bi = map(int, input().split())
    a_sum += ai
    diff.append(ai-bi)
diff.sort(reverse = True)

gap = a_sum - m
count = 0
for i in range(n):
    if(gap <= 0):
        break
    gap-=diff[i]
    count+=1
   
if(gap>0):
    print(-1)
else:
    print(count)



