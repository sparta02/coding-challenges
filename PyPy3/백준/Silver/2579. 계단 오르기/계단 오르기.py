n=int(input())
arr=[]

for _ in range(n):
    arr.append(int(input()))

#dp[i][j]
# i번째 계단에서
# 연속으로 1칸 올라간게 j(0~1)번일 때
# 최댓값

dp= [ [0]*2 for _ in range(n)]
dp[0][0]=arr[0]
if n>=2:
    dp[1][0]=arr[1]
    dp[1][1]=arr[0]+arr[1]

for i in range(2, n):
    # 연속으로 1칸 올라간게
    # 0번이기 위해선 2칸 점프
    dp[i][0]=max(dp[i-2])+arr[i]

    # 1번이기 위해선 dp[i-1][0]
    if dp[i-1][0]!=0:
        dp[i][1]=dp[i-1][0]+arr[i]



# for i in range(n):
#     for j in range(2):
#         print(dp[i][j], end=" ")
#     print()
# print()

print(max(dp[-1]))