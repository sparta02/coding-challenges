n, k = map(int, input().split())
arr = list(map(int, input().split()))

result=0
# Please write your code here.
maps={}

for num in arr:
    if k-num in maps:
        result+=maps[k-num]

    if num in maps:
        maps[num]+=1
    else:
        maps[num]=1

print(result)


