n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
temp_grid=[row[:] for row in grid]

def reset_grid(k):
    global temp_grid
    temp_grid=[row[:] for row in grid]
    for i in range(n):
        for j in range(n):
            if temp_grid[i][j]<k:
                temp_grid[i][j]=999

def print_grid(하이):
    for i in range(n):
        for j in range(n):
            print(하이[i][j], end=" ")
        print()
    print()



def calc_grid(k):
    dp= [[0]*n for _ in range(n)]
    dp[0][0]=temp_grid[0][0]

    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1], temp_grid[0][i])
        dp[i][0] = max(dp[i-1][0], temp_grid[i][0])
    
    for i in range(1,n):
        for j in range(1,n):
            dp[i][j]=max(min(dp[i-1][j],dp[i][j-1]), temp_grid[i][j])
    
    if dp[n-1][n-1]==999:
        return 999
    else:
        return dp[n-1][n-1] - k
    #print_grid(dp)

result=9999

for k in range(101):
    reset_grid(k)
    #print_grid(temp_grid)
    
    result=min(result, calc_grid(k))

print(result)
    
