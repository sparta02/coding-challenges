n = int(input())
people = [list(input().split()) for _ in range(n)]
for i in range(n):
    people[i][0] = int(people[i][0])

# 위치 기준 정렬
people.sort(key=lambda x: x[0])

result = 0

for i in range(n):
    g = 0
    h = 0
    for j in range(i, n):
        if people[j][1] == "G":
            g += 1
        else:
            h += 1

        # 전부 G이거나 전부 H
        if h == 0 or g == 0:
            result = max(result, people[j][0] - people[i][0])

        # G == H
        if g == h:
            result = max(result, people[j][0] - people[i][0])

print(result)
