import sys

# 입력을 받습니다.
N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# 두 숫자 사이의 원형 거리가 2 이내인지 확인하는 함수
def is_close(n, target, N):
    # 시계 방향 거리와 반시계 방향 거리 중 작은 값이 2 이하여야 함
    diff = abs(n - target)
    dist = min(diff, N - diff)
    return diff <= 2 or diff>=(N-2)

cnt = 0

# 모든 가능한 조합(i, j, k)을 확인합니다.
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            # 첫 번째 조합과 가까운지 확인
            match1 = is_close(i, a1, N) and is_close(j, b1, N) and is_close(k, c1, N)
            
            # 두 번째 조합과 가까운지 확인
            match2 = is_close(i, a2, N) and is_close(j, b2, N) and is_close(k, c2, N)
            
            # 둘 중 하나라도 만족하면 카운트 (합집합 개념이 OR 연산에 포함됨)
            if match1 or match2:
                cnt += 1

print(cnt)