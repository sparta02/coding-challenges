import sys
# 입력 속도 최적화 (N이 작아서 필수는 아니지만 습관적으로 사용)
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 우(0), 하(1), 좌(2), 상(3)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def simulate(sx, sy, sd):
    x, y, way = sx, sy, sd
    count = 1
    # 안전장치: n*n*4번 이상 움직였다면 무한 루프임
    limit = n * n * 4
    move_tick = 0
    
    while 0 <= x < n and 0 <= y < n:
        move_tick += 1
        if move_tick > limit: return count # 무한 루프 강제 종료
        
        if grid[x][y] == 1: # / 거울
            # 0<->3, 1<->2
            way = 3 - way
        elif grid[x][y] == 2: # \ 거울
            # 0<->1, 2<->3
            way = way ^ 1 # 비트 연산 혹은 조건문으로 명확히
            
        x += dx[way]
        y += dy[way]
        count += 1
    return count

result = 0

for i in range(n):
    # 위에서 아래로 (x=0, y=i, 하향)
    result = max(result, simulate(0, i, 1))
    # 아래에서 위로 (x=n-1, y=i, 상향)
    result = max(result, simulate(n-1, i, 3))
    # 왼쪽에서 오른쪽으로 (x=i, y=0, 우향)
    result = max(result, simulate(i, 0, 0))
    # 오른쪽에서 왼쪽으로 (x=i, y=n-1, 좌향)
    result = max(result, simulate(i, n-1, 2))

print(result)