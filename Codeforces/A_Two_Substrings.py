string = input()
lo = 0
hi = 1
if(len(string)<2):
     print("NO")
while(hi<len(string)-2):
     if((string[lo]=="A"and string[hi]=="B") or (string[lo]=="B"and string[hi]=="A")):
          print("YES")
          break
     lo+=hi
     hi+=1
print("NO")