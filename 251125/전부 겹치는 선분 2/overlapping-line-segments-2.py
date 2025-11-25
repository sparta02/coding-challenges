n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

# Please write your code here.

# 1. 1~100까지 좌표를 저장하는 배열 arr 선언
# 2. 각 선분들이 속해있는 좌표를 배열 arr에 기록
# 3. 1개의 좌표라도 전체 선분의 수의 값이 저장되어 있다면 -> True

arr=[0]*101

for i in range(n): # 각 선분들에 대해
    for j in range(x1[i], x2[i]+1): # 모든 점을 탐색하며 1을 추가
        arr[j]+=1

if n-1 in arr:
    print("Yes")
else:
    print("No")