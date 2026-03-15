s = input()
count = 0
maxlen = 0
stack = [-1]

for i,char in enumerate(s):
    if char == "(":
        stack.append(i)
    else:
        stack.pop()
        if not stack:
           stack.append(i)
        else:
           l = i-stack[-1]
           if l > maxlen:
               maxlen = l
               count = 1
           elif l == maxlen:
               count+=1
if maxlen == 0:
    print(0,1)   
else:
    print(maxlen,count)
