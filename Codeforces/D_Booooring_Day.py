for _ in range(int(input())):
    n,l,r = map(int,input().split())
    decks = list(map(int,input().split()))
    _sum = 0
    count = 0
    left = 0
    for right in range(len(decks)):
        _sum += decks[right]
        
        while _sum > r:
            _sum-=decks[left]
            left+=1
        
        if(l<= _sum <=r):
            count+=1
            _sum = 0
            left = right+1
    print(count)

