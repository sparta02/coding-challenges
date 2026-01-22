n,m = map(int, input().split())
nums = list(map(int, input().split()))

# dp[n][j]를
# 숫자 n까지 고려했을 때, j를 만들 수 있는 경우의 수

def print_dp():
    for i in range(n):
        for j in range(41):
            print(dp[i][j], end=" ")
        print()
    print()

# offset은 +20으로 설정
dp=[ [0]*41 for _ in range(n)]

dp[0][nums[0]+20]+=1
dp[0][-nums[0]+20]+=1

for i in range(1, n):
    for j in range(41):
        
        if 0<= j-nums[i] <=40 and dp[i-1][j-nums[i]]:
            dp[i][j]+=dp[i-1][j-nums[i]]
        if 0<=j+nums[i]<=40 and dp[i-1][j+nums[i]]:
            dp[i][j]+=dp[i-1][j+nums[i]]
print(dp[-1][m+20])