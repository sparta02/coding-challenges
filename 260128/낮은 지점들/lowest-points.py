n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
maps={}

for point in points:
    x=point[0]
    y=point[1]
    if x in maps:
        maps[x]=min(maps[x],y)
    else:
        maps[x]=y

print(sum([x for x in points.values()]))