n, k = map(int, input().split())
nums = list(map(int, input().split()))

if k == 1:
    print(nums[-1] - nums[0])
else:
    gaps = []
    for i in range(1, n):
        gaps.append(nums[i] - nums[i-1])

    gaps.sort(reverse=True)

    print(nums[-1] - nums[0] - sum(gaps[:k-1]))
