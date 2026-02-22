for _ in range(int(input())):
    n = int(input())
    s = input()
    if "." not in s:
        print(0)
        continue
    if("..." in s):
        print(2)
        continue
    else:
        print(s.count("."))
        
            
