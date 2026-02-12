A=list(input())
B=list(input())

dp=[ [0]*len(A) for _ in range(len(B))]

def print_grid(grid):
    print("  ", end="")
    for i in range(len(A)):
        print(A[i], end=" ")
    print()
    for i in range(len(grid)):
        print(B[i], end=" ")
        for j in range(len(grid[0])):
            print(grid[i][j], end=" ")
        print()
    print()

if A[0]==B[0]:
    dp[0][0]=1
else:
    dp[0][0]=0

for i in range(1, len(A)):
    if B[0]==A[i]:
        dp[0][i]=1
    else:
        dp[0][i]=dp[0][i-1]

for j in range(1, len(B)):
    if B[j]==A[0]:
        dp[j][0]=1
    else:
        dp[j][0]=dp[j-1][0]

for i in range(1, len(B)):
    for j in range(1, len(A)):
        if A[j]==B[i]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])

# print_grid(dp)
print(dp[-1][-1])