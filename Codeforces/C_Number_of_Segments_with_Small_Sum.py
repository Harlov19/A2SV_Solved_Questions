n,s = map(int,input().split())
nums = list(map(int,input().split()))
left = 0
count = 0
wind_sum = 0
for right in range(n):
    wind_sum += nums[right]
    while left<=right and wind_sum > s:
        wind_sum-=nums[left]
        left+=1
    count+= right-left+1
   
print(count)
