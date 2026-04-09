n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
points.sort()

maps_a={}
maps_b={}

for i, p in enumerate(points):
    maps_a[i]=p
    maps_b[p]=i

for a, b in queries:
    print(maps_b[b]-maps_b[a]+1)

