N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

arr.sort()

result=0

for i in range(N):
    count=1
    for j in range(i+1, N):
        if j-i<=K:
            count+=1
        else:
            break
    result=max(result, count)

print(result)