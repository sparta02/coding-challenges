from collections import deque

n, k = map(int, input().split())

queue=deque()
queue.append((n, 0))
visited=[-1]*100001

min_time=10**9
count=0

while queue:
    curr, time = queue.popleft()

    # 목표 도달 시
    if curr == k:
        # 최초 거리 1번
        if time < min_time:
            min_time = time
            count = 1
        elif time == min_time:
            count += 1
        continue

    for next_pos in (curr - 1, curr + 1, curr * 2):
        if 0 <= next_pos <= 100000:
            # 처음 방문하거나, 이전에 방문했더라도 같은 최단 시간으로 도착한 경우
            if visited[next_pos] == -1 or visited[next_pos] == time + 1:
                visited[next_pos] = time + 1
                queue.append((next_pos, time + 1))
print(min_time)
print(count)