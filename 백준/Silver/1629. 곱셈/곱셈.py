a, b, c=map(int, input().split())

maps={}
maps[1]=a%c

def calc(num):
    if num in maps:
        return maps[num]
    
    
    temp=int(num/2)
    calc(temp)
    calc(num-temp)
    maps[num]=(maps[temp]*maps[num-temp])%c

calc(b)
print(maps[b])