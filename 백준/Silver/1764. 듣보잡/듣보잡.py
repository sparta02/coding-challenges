import heapq
import sys
input= sys.stdin.readline

maps={}
n, m = map(int, input().split())
for _ in range(n):
    name=input().strip()
    maps[name]=1

name_list=[]
for _ in range(m):
    name=input().strip()
    if name in maps:
        name_list.append(name)
name_list.sort()
print(len(name_list))

for nam in name_list:
    print(nam)

