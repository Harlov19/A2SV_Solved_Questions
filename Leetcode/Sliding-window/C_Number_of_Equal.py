n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

_count = 0
i = j = 0

while i<n and j<m:
    if(a[i] == b[j]):
        count_a = 1
        while i+1 < n and a[i] == a[i+1]:
            count_a += 1
            i+=1
        count_b = 1
        while j+1 < m and b[j] == b[j+1]:
            count_b+=1
            j+=1
        _count+= (count_a*count_b)
        i+=1
        j+=1
    elif(a[i]<b[j]):
        i+=1
    else:
        j+=1

print(_count)
