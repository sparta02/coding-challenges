n, m = map(int, input().split())

maps={}

for _ in range(n):
    a, b = input().split()
    maps[a]=b

for _ in range(m):
    temp=input()
    print(maps[temp])