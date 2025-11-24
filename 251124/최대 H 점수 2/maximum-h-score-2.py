N, L = map(int, input().split())
arr = list(map(int, input().split()))

max_h = 0

# 가능한 모든 H 값을 확인 (0부터 N까지)
for h in range(N + 1):
    # 현재 h 이상인 원소 개수
    count_ge_h = sum(1 for x in arr if x >= h)
    
    # 이미 조건을 만족하면
    if count_ge_h >= h:
        max_h = max(max_h, h)
        continue
    
    # 부족한 개수
    needed = h - count_ge_h
    
    # h 미만인 원소들 중에서 h-1인 원소 개수
    # (이들을 1 증가시키면 h가 됨)
    count_h_minus_1 = sum(1 for x in arr if x == h - 1)
    
    # h-1인 원소가 충분하고, L 범위 내라면 가능
    if count_h_minus_1 >= needed and needed <= L:
        max_h = max(max_h, h)

print(max_h)