for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort(reverse = True)
    score = 0
    for r in range(1,len(nums),2):
        score+=nums[r]
    print(score)
