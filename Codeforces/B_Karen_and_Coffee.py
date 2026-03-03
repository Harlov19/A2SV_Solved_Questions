n,k,q = map(int,input().split())
recipes = [ ]
for _ in range(n):
    li,ri = map(int,input().split())
    recipes.append([li,ri])
questions = []
for _ in range(q):
    a,b = map(int,input().split())
    questions.append([a,b])

size = 200000 + 2
tmp = [0]*size
for i in range(n):
    li,ri = recipes[i]
    tmp[li]+=1
    tmp[ri+1]-=1

prefix = [0]*size
prefix[0] = 0
for i in range(1,size):
    prefix[i] = prefix[i-1]+tmp[i]

admissible = [0]*size
for i in range(1, size):
    admissible[i] = 1 if prefix[i] >= k else 0

s_prefix = [0]*size
for i in range(1,size):
    s_prefix[i] = s_prefix[i-1] + admissible[i]
for a,b in questions:
    print(s_prefix[b]-s_prefix[a-1])
