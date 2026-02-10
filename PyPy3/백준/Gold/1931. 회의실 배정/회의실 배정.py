n = int(input())
meetings = []

for _ in range(n):
    a, b = map(int, input().split())
    meetings.append((a, b))

if n == 0:
    print(0)
    exit()

meetings.sort(key=lambda x: (x[1], x[0]))

result = 1
last_end = meetings[0][1]

for i in range(1, n):
    if meetings[i][0] >= last_end:
        result += 1
        last_end = meetings[i][1]

print(result)
