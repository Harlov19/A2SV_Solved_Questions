
brackets = input()
count = 0
for bracket in brackets:
    if(bracket=="("):
        count+=1
    else:
        if(count==0):
            print("NO")
            break
        count-=1
else:
    print("YES") if count==0 else print("NO")
