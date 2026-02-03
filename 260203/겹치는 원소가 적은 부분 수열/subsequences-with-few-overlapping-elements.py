n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
i,j=0,0
result=0

maps={}

for i in range(n):
    while j<n and (arr[j] not in maps or maps[arr[j]]<k):
        maps[arr[j]]=maps.get(arr[j],0)+1
        j+=1
    # print(i)
    # print(maps)
    result=max(result, j-i)
    maps[arr[i]]-=1

print(result)