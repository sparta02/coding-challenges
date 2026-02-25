t=int(input())


for _ in range(t):
    n=int(input())
    maps={}
    for _  in range(n):
        cloth, type= input().split()
        maps[type]=maps.get(type, 0)+1
    # print(maps)

    clothes=[]
    for _, value in maps.items():
        clothes.append(value)
    # print(clothes)
    result=1

    for i in clothes:
        result*=(i+1)
    print(result-1)


