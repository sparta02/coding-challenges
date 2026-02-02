n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
i, j= 0,0
result=0
maps={}

for i in range(n):
    #print(arr[i])
    # j가 인덱스를 초과하지 않고 0번 나왔다면
    while (j<n and arr[j] not in maps):
        maps[arr[j]]=1
        j+=1

    result=max(result, j-i)
    #print(maps)
    maps.pop(arr[i])

print(result)
