t = int(input())
for _ in range(t):
    keys_doors = input()
    keys = set()
    for char in keys_doors:
        if(char =="r" or char =="g" or char =="b"):
            keys.add(char)
        else:
            if(char.lower() not in keys):
                print("NO")
                break
            else:
              keys.remove(char.lower())  
    else:
        print("YES")
