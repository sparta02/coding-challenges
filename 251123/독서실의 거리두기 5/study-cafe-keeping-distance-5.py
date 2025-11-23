N = int(input())
seat = input()

arr = [i for i in range(N) if seat[i] == "1"]

result = 0

# 첫 번째 사람과 왼쪽 끝 거리
result = max(result, arr[0])

# 마지막 사람과 오른쪽 끝 거리
result = max(result, N - 1 - arr[-1])

# 가운데 사람들 사이 거리의 절반
for i in range(1, len(arr)):
    dist = (arr[i] - arr[i-1]) // 2
    result = max(result, dist)

print(result)
