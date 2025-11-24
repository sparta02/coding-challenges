N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

arr.sort()

result=0

for i in range(N):
    count=0
    for j in range(i, N):
        #print(i, j)
        if arr[j]-arr[i]<=K:
            count+=1
        else:
            break
    result=max(result, count)

print(result)