N, L = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

def can_make(H):
    # H개가 H 이상이 되도록 만들 수 있는지 확인
    need = 0
    for i in range(min(H, N)):
        if arr[i] < H:
            need += H - arr[i]
    return need <= L

# 이분 탐색으로 최대 H 찾기
left, right = 0, N
answer = 0
while left <= right:
    mid = (left + right) // 2
    if can_make(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
