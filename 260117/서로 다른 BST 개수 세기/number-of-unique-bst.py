n = int(input())

# Please write your code here.

dp=[0]*20

dp[0]=1
dp[1]=1
dp[2]=2

# i=3
# root가 1
# 왼쪽 0, 오른쪽 2

# root가 2
# 1, 1

# root가 2
# 왼쪽 2, 오른쪽 0
#############################
# i=4
# root가 1
# 왼쪽 0, 오른쪽 3

# root가 2
# 1, 2

# root가 3
# 왼쪽 2, 오른쪽 1

# root가 4
# 왼쪽 3, 오른쪽 0
for i in range(3, n+1):
    temp=0
    for j in range(i):
        temp+=dp[j]*dp[i-j-1]
    dp[i]=temp

print(dp[n])