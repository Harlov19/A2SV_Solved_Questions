for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    if n == 1:
        print(1, "\n", *arr)
    ans = [arr[0]] 
    f = 1
    s = 1
    turn = 0 #Increasing ,0 =>Decreasing
    if(arr[0]<arr[1]):
        turn = 1
    
    while s < n:
        if(turn == 1):
            if(arr[s-1]> arr[s]):
                ans.append(arr[s-1])
                f = s
                turn = 0
        else:
            if(arr[s-1] < arr[s]):
                ans.append(arr[s-1])
                f = s
                turn = 1
        s+=1
           

    ans.append(arr[-1])
    print(len(ans))
    print(*ans)
