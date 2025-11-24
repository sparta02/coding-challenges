N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

explode_count = {}

for i in range(N):
    cur = num[i]
    exploded = False

    # 현재 폭탄 기준 거리 K 범위 확인
    for j in range(max(0, i-K), min(N, i+K+1)):
        if i != j and num[j] == cur:
            exploded = True
            break

    # 폭발한다면 카운트 증가
    if exploded:
        explode_count[cur] = explode_count.get(cur, 0) + 1

# 아무 폭탄도 터지지 않았을 경우
if not explode_count:
    print(0)
else:
    # 가장 많이 터진 번호, 동점일 경우 번호가 큰 것 선택
    max_count = max(explode_count.values())
    candidates = [num for num, cnt in explode_count.items() if cnt == max_count]
    print(max(candidates))
