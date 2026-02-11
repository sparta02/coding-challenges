n=int(input())

arr=[]

for _ in range(n):
    temp=list(map(int, input().split()))
    arr.append(temp)

dp=[]
for i in range(n):
    dp.append([-1]*(i+1))

dp[0][0]=arr[0][0]

# i번째 줄에서
for i in range(n-1):
    # j번째 원소
    for j in range(i+1):
        dp[i+1][j]=max(dp[i+1][j], dp[i][j]+arr[i+1][j])

        dp[i+1][j+1]=max(dp[i+1][j+1], dp[i][j]+arr[i+1][j+1])

print(max(dp[-1]))
