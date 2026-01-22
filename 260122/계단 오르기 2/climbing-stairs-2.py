n = int(input())
coin = [0] + list(map(int, input().split()))


#dp[i][j]를 i번째 숫자까지 고려했을 때 
#1칸만 점프하는 걸 j번째 한다면?

dp=[ [-1]*4 for _ in range(n+1) ]

def print_grid():
    for i in range(n+1):
        for j in range(4):
            print(dp[i][j], end=" ")
        print()
    print()

dp[0][0]=0
dp[0][1]=0
dp[0][2]=0
dp[0][3]=0
dp[1][0]=-1
dp[1][1]=coin[1]
dp[1][2]=-1
dp[1][3]=-1
dp[2][0]=coin[2]
dp[2][1]=-1
dp[2][2]=dp[1][1]+coin[2]
dp[2][3]=-1

for i in range(2, n+1):
    if dp[i-2][0] != -1:
        dp[i][0]=dp[i-2][0]+coin[i]
    dp[i][1]=max(dp[i-1][0]+coin[i], dp[i-2][1]+coin[i])
    dp[i][2]=max(dp[i-1][1]+coin[i], dp[i-2][2]+coin[i])
    dp[i][3]=max(dp[i-1][2]+coin[i], dp[i-2][3]+coin[i])
# print_grid()
print(max(dp[-1]))
