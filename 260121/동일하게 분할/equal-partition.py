n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
목표길이=int(sum(arr)/2)

dp=[[-1]*(목표길이+1) for _ in range(n)]

dp[0][0]=0
dp[0][arr[0]]=arr[0]

for i in range(1, n):
    for j in range(목표길이+1):
        dp[i][j]=max(dp[i][j], dp[i-1][j])
        if j>=arr[i] and dp[i-1][j-arr[i]] !=-1:
            dp[i][j]=max(dp[i][j], dp[i-1][j-arr[i]]+arr[i])

# for i in range(n):
#     for j in range(목표길이+1):
#         print(dp[i][j], end=" ")
#     print()
# print()

if sum(arr)%2 ==1:
    print("No")
else:
    if dp[-1][목표길이]!=-1:
        print("Yes")
    else:
        print("No")