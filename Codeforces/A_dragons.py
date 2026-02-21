s,n = map(int,input().split());
arr = []
for i in range(n):
   x,y = list(map(int,input().split()))
   arr.append([x,y])
arr.sort(key=lambda x:x[0])
wins = True
for strength,bonus in arr:
   if(strength>s):
      wins =False
      break
   s+=bonus
print("Yes") if wins else print("NO")
   
