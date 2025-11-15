x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.

arr=[[0]*2001 for i in range(2001)]

for j in range(x1[0]+1000, x2[0]+1000):
        for k in range(y1[0]+1000, y2[0]+1000):
            arr[j][k]=1



for j in range(x1[1]+1000, x2[1]+1000):
        for k in range(y1[1]+1000, y2[1]+1000):
            arr[j][k]=0



min_x=10000
min_y=10000
max_x=-1
max_y=-1

for i in range(2001):
    for j in range(2001):
        if arr[i][j]==1:
            if min_x>i:
                min_x=i
            if min_y>j:
                min_y=j
            if max_x<i:
                max_x=i
            if max_y<j:
                max_y=j

print((max_x-min_x+1)*(max_y-min_y+1))
            