for _ in range(int(input())):
    a, b = map(int, input().split())
    
    ans = float('inf')
    
    for inc in range(0, 30):
        new_b = b + inc
        
        if new_b == 1:
            continue
        
        curr_a = a
        ops = inc
        
        while curr_a > 0:
            curr_a //= new_b
            ops += 1
        
        ans = min(ans, ops)
    
    print(ans)
