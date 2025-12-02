n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]



# 1. 세로 3칸짜리 블록의 합을 반환하는 sum_col
def sum_col(a, b):
    return grid[a][b] + grid[a+1][b] + grid[a+2][b]

# 2. 가로 3칸짜리 블록의 합을 반환하는 sum_row
def sum_row(a, b):
    return grid[a][b] + grid[a][b+1] + grid[a][b+2]

# 3. ㄴ자 블록이 들어가는 4가지 경우의 수 중 가장 큰 값을 반환하는 sum_tri
def sum_tri(a, b):
    sum_arr=[]
    sum_arr.append(grid[a][b])
    sum_arr.append(grid[a+1][b])
    sum_arr.append(grid[a][b+1])
    sum_arr.append(grid[a+1][b+1])

    sum_temp=0
    for i in range(4):
        sum_temp= max(sum_temp, sum(sum_arr)-sum_arr[i] )
    return sum_temp




# 4. 모든 경우의 수를 테스트 하는 main 코드
result=0
# 4-1. sum_col 호출
for i in range(n-2): # x축의 개수보다 2칸 적게 호출
    for j in range(m):
        result=max(result, sum_col(i, j))

# 4-2. sum_row 호출
for i in range(n): 
    for j in range(m-2): # y축의 개수보다 2칸 적게 호출
        result=max(result, sum_row(i, j))

# 4-3. sum_tri 호출
for i in range(n-1): 
    for j in range(m-1):
        result=max(result, sum_tri(i, j))
        

print(result)