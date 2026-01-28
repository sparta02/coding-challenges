n, k = map(int, input().split())
arr = list(map(int, input().split()))

maps={}

for num in arr:
    maps[num]= maps.get(num, 0)+1

result=0

for i in range(n):
    maps[arr[i]]-=1
    for j in range(i+1, n):
        maps[arr[j]]-=1
        # 2개의 숫자를 선택하고
        # k-arr[i]-arr[j]가 몇 개 있는지 파악
        target_num=k-arr[i]-arr[j]
        result+=maps.get(target_num, 0)
        #print(arr[i], arr[j], target_num, result)
        maps[arr[j]]+=1
    maps[arr[i]]+=1

print(int(result/3))