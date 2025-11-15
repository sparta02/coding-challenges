n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
arr=[[[0] for i in range(200)]
for i in range(200)]

def fill(x1, y1, x2, y2):
    global arr
    print
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j]=1

for i in range(n):
    fill(x1[i], y1[i], x2[i], y2[i])

cnt=0
for i in range(200):
        for j in range(200):
            if arr[i][j]==1:
                cnt+=1

print(cnt)