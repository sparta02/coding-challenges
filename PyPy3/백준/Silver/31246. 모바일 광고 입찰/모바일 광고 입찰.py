n, k = map(int,input().split())

temp=[ list(map(int, input().split())) for _ in range(n)]

arr=[a-b for a, b in temp]
arr.sort(reverse=True)
# print(arr)
target=arr[k-1]
if target>=0:
    print(0)
else:
    print(abs(target))