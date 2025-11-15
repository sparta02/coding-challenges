x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.

arr=[[0]*2001 for i in range(2001)]

for i in range(x1[0], x2[0]):
    for j in range(y1[0], y2[0]):
        arr[i][j]=1

for i in range(x1[1], x2[1]):
    for j in range(y1[1], y2[1]):
        arr[i][j]=1

for i in range(x1[2], x2[2]):
    for j in range(y1[2], y2[2]):
        arr[i][j]=0

cnt=0
for i in range(len(arr)):
    for j in range(len(arr)):
        cnt+=arr[i][j]

print(cnt)

    