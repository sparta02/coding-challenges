n=int(input())

arr=[]

for _ in range(n):
    temp=int(input())
    arr.append(temp)

dp=[0]*(max(arr)+1)

dp[1]=1
dp[2]=2
dp[3]=4
for i in range(4, max(arr)+1):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

for num in arr:
    print(dp[num])