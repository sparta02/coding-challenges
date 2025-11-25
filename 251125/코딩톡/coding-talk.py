n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]

# u 기준으로 정렬
messages_sorted = sorted(
    [(i, msg[0], int(msg[1])) for i, msg in enumerate(messages)],
    key=lambda x: x[2]
)

# 정렬 후 p가 어디로 갔는지 찾기
original_p_index = p - 1
for new_idx, (old_idx, c, u) in enumerate(messages_sorted):
    if old_idx == original_p_index:
        p_new = new_idx
        break

# 정렬된 리스트에서 다시 c, u 분리
c = [item[1] for item in messages_sorted]
u = [item[2] for item in messages_sorted]

arr = [chr(65 + i) for i in range(n)]

# p 메시지 보낸 사람 제거
if c[p_new] in arr:
    arr.remove(c[p_new])

# p 이후 메시지 보낸 사람 제거 (정렬 기반)
for i in range(p_new + 1, m):
    if c[i] in arr:
        arr.remove(c[i])

# u[p_new]가 0이 아닌 경우에만 출력
if u[p_new] != 0:
    for x in arr:
        print(x, end=" ")
