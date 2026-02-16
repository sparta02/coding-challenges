n, m = map(int, input().split())
maps={}

for i in range(1, n+1):
    temp=input()
    maps[temp]=str(i)
    maps[str(i)]=temp

for _ in range(m):
    temp=input()
    print(maps[temp])