n = int(input())
cards=list(map(int, input().split()))

maps={ value:key for key, value in enumerate(cards)}
point=[0]*n
# print(maps)

for index in range(n):
    num=cards[index]
    # print(f"{num} turn")
    for i in range(1, int(num**0.5)+1):
        if num%i==0:
            a=i
            b=num//i
            if a in maps:
                # print(a)
                point[maps[a]]+=1
                point[index]-=1
            if a!=b and b!=num and b in maps:
                # print(b)
                point[maps[b]]+=1
                point[index]-=1
print(*point)