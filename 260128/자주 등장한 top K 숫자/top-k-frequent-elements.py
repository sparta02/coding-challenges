n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
maps={}

for i in range(n):
    maps[arr[i]]=maps.get(arr[i],0)+1

count_list=list(maps.items())

count_list=sorted(count_list, key=lambda x: (-x[1],-x[0]))

for i in range(k):
    print(count_list[i][0], end=" ")