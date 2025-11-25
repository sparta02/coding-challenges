n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

# Please write your code here.
arr=[0]*101

for i in range(n): # 각 선분들에 대해
    for j in range(x1[i], x2[i]+1): # 모든 점을 탐색하며 1을 추가
        arr[j]+=1

if n in arr:
    print("Yes")
else:
    print("No")