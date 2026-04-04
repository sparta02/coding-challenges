import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
x=int(input())

maps={}
for num in arr:
    maps[num]=maps.get(num, 0)+1
# print(maps)

cnt=0
for num in arr:
    temp=x-num
    if temp in maps:
        cnt+=1

print(cnt//2)
