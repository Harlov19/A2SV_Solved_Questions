n = int(input())
arr = []
for i in range(n):
    l, r = map(int, input().split())
    arr.append((l, r, i + 1)) 


arr.sort(key=lambda x: (x[0], -x[1]))

maxRight = [arr[0][1], arr[0][2]] 
for i in range(1, n):
    if arr[i][1] <= maxRight[0]:
       
        print(arr[i][2], maxRight[1]) 
        break
    else:
        maxRight = [arr[i][1], arr[i][2]]
else:
    print(-1, -1)
