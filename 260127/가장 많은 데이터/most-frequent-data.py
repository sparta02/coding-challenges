n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
maps={}
result=0
for w in words:
    if w in maps:
        maps[w]+=1
    else:
        maps[w]=1
    result=max(result, maps[w])

print(result)