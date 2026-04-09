n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 누적합 배열 선언
prefix_sum= [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        prefix_sum[i][j]=grid[i-1][j-1]+prefix_sum[i-1][j]+prefix_sum[i][j-1]-prefix_sum[i-1][j-1]

def print_grid(grid):
    for i in range(len(grid)):
        print(*grid[i])

# (x1, y1)~ (x2, y2)의 합 반환
def calc_sum(x1, y1, x2, y2):
    return prefix_sum[x2+1][y2+1]-prefix_sum[x2+1][y1]-prefix_sum[x1][y2+1]+prefix_sum[x1][y1]


result=0
for x1 in range(n):
    for x2 in range(x1, n):
        for y1 in range(m):
            for y2 in range(y1, m):
                for x3 in range(n):
                    for x4 in range(x3, n):
                        for y3 in range(m):
                            for y4 in range(y3, m):
                                # (x1~x2), (y1~y2)
                                # (x3~x4), (y3~y4)
                                if (x1<=x3<=x2 and y1<=y3<=y2) or (x1<=x4<=x2 and y1<=y4<=y2):
                                    continue
                                # print(x1,y1,x2,y2)
                                # print(x3,y3,x4,y4)
                                # print()
                                result=max(result, calc_sum(x1,y1,x2,y2)+calc_sum(x3,y3,x4,y4))

print(result)