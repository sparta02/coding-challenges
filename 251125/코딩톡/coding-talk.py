n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

people = [chr(ord('A') + i) for i in range(n)]

# p번째 메시지를 보낸 사람
sender_p = c[p-1]

# p번째 이후에 메시지를 보낸 사람들 (읽었음이 확실한 사람)
sure_read = set()
for i in range(p, m):
    sure_read.add(c[i])

# p번째 메시지 보낸 사람도 읽었음이 확실
sure_read.add(sender_p)

# 읽지 않았을 가능성이 있는 사람
possible = [x for x in people if x not in sure_read]

print(*possible)
