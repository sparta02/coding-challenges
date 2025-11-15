n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.

arr=[[0]*201 for i in range(201)]

for i in range(n):
    for j in range(x[i]+100, x[i]+108):
        for k in range(y[i]+100, y[i]+108):
            arr[j][k]=1

cnt=0
for j in range(201):
    for k in range(201):
        cnt+=arr[j][k]
print(cnt)