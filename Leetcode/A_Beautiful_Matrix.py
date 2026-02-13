matrix = [list(map(int,input().split())) for i in range(5)]
for row in range(5):
    for col in range(5):
        if(matrix[row][col] == 1):
            print(abs(row-2)+abs(col-2))
            break
