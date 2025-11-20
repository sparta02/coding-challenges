N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

left = [r[0] for r in ranges]
right = [r[1] for r in ranges]

result = 0

# 가능한 모든 온도 T에 대해 작업량 계산
for T in range(min(left) - 1, max(right) + 2):
    total = 0
    for Ta, Tb in ranges:
        if T < Ta:
            total += C
        elif T <= Tb:
            total += G
        else:
            total += H
    result = max(result, total)

print(result)
