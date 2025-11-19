n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

def calc_dist(x1, y1, x2, y2):
    return (x1-x2)**2+(y1-y2)**2


result = 999999999
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        result=min(result, calc_dist(x[i],y[i],x[j],y[j]))

print(result)
        