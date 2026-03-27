n=int(input())
arr= [ list(map(int, input().split())) for _ in range(n)]

arr.sort()
# print(arr)
result=0

new=[temp[1] for temp in arr]
# print(new)
dp=[1]*n

for i in range(1, n):
    for j in range(i):
        if new[j]<new[i]:
            dp[i]=max(dp[i], dp[j]+1)

print(n-max(dp))