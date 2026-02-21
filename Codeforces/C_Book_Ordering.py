n = int(input())
books = []
for _ in range(n):
    w,h = map(int,input().split())
    books.append([w,h])
ans = [max(books[0][0],books[0][1])]
for i in range(1,n):
    if(books[i][0]>ans[i-1] and books[i][1]>ans[i-1]):
        print("NO")
        break
    else:
         a = ""
         if books[i][0]<=ans[i-1] and books[i][1]<=ans[i-1]:
             a = max(books[i][0],books[i][1])
         elif(books[i][1]<=ans[i-1]):
             a = books[i][1]
         else:
             a = books[i][0]
       
         ans.append(a) 
else:
    print("YES")
