X = int(input())

# t초 동안 도달할 수 있는 최대 이동 거리 계산
def max_dist(t):
    # t초 중에서, 1로 시작하고 1로 끝나는 속도 패턴을 만들 때
    # 가장 멀리 갈 수 있는 거리 계산

    # 증가 가능한 단계 수
    up = (t - 1) // 2
    # 감소도 동일
    down = up

    # 남는 초(속도 유지)
    remain = t - (up + down + 1)

    # 최고 속력
    vmax = 1 + up

    # 증가 구간 거리: 1 + 2 + ... + vmax
    up_dist = (1 + vmax) * up // 2

    # 감소 구간 거리: vmax + ... + 1
    down_dist = (vmax + 1) * down // 2

    # 마지막 1m/s 유지 포함
    stay_dist = 1 * (remain + 1)

    return up_dist + down_dist + stay_dist


t = 1
while True:
    if max_dist(t) >= X:
        print(t)
        break
    t += 1
