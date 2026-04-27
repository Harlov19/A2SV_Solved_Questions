t = int(input())
for _ in range(t):
    n = int(input())
    enemy = list(map(int,input().strip()))
    dawit = list(map(int,input().strip()))

    count = 0
    for i,cell in enumerate(dawit):
        if cell == 1:
            if enemy[i] == 0:
                count+=1
                enemy[i] = -1
                
            elif i-1>=0  and enemy[i-1] == 1:
                count+=1
                enemy[i-1] = -1
            elif i+1 < n and enemy[i+1] == 1:
                count+=1
                enemy[i+1] = -1
    print(count)
