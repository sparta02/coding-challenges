n=int(input())
arr1=list(map(int, input().split()))
maps={}
for num in arr1:
    maps[num]=1
m=int(input())
arr2=list(map(int, input().split()))

for i in range(m):
    if arr2[i] in maps:
        print(1)
    else:
        print(0)