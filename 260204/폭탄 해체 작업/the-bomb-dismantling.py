N = int(input())
bombs = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
#bombs.sort(key=lambda x: x[1])

# print(bombs)

maps={}
for score, time in bombs:
    maps[time]=max(maps.get(time, 0), score)

print(sum(list(maps.values())))
