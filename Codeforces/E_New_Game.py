for _ in range(int(input())):
    n,k = map(int,input().split())
    decks = list(map(int,input().split()))
    
    decks.sort()
  
    maxc = 1
    l = 0
    for r in range(n):
       if r-1>=0 and decks[r] != decks[r-1] and decks[r] != decks[r-1]+1:
        l = r
       
       while l<r and decks[r]-decks[l]+1 >k:
        l+=1  
       maxc = max(maxc,r-l+1)
    print(maxc)





