n = int(input())
points = list(map(int,input().split()))
points.sort()
mid = 0
if(n%2 == 0):
    mid = n//2
else:
    mid = (n+1)//2

print(points[mid-1])

