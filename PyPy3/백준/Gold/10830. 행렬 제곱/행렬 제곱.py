import sys

n, b = map(int, input().split())

grid= [ list(map(int, input().split())) for _ in range(n)]

# 행렬 곱셈 함수
def mult(A, B):
    result_grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = 0
            for k in range(n):
                temp += A[i][k] * B[k][j]
            result_grid[i][j] = temp % 1000
    return result_grid

# 분할 정복을 이용한 거듭제곱
def power(matrix, exp):
    if exp == 1:
        for i in range(n):
            for j in range(n):
                matrix[i][j] %= 1000
        return matrix
    
    # 절반으로 나누어 계산
    half = power(matrix, exp // 2)
    
    # 지수가 짝수라면: half * half
    if exp % 2 == 0:
        return mult(half, half)
    # 지수가 홀수라면: half * half * matrix
    else:
        return mult(mult(half, half), matrix)

# 결과 계산 및 출력
result = power(grid, b)

for row in result:
    print(*(row))