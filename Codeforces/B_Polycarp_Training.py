n = int(input())
constests = list(map(int,input().split()))
constests.sort()
k = 0

for i in range(len(constests)):
    if(constests[i] >= k+1):
        k+=1
print(k)
