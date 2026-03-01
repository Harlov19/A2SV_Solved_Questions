n = int(input())
s = input()
k = 0
for char in s:
    if char == "H":
        k+=1

maxH = 0
currH = 0
for char in s[:k]:
    if  char == "H":
        currH+=1
maxH = currH
l = 0
for r in range(k,2*n):
    if s[r%n] == "H":
        currH+=1
    
    if s[l%n] == "H":
        currH-=1
    l+=1
    maxH  = max(maxH,currH)
print(k-maxH)

