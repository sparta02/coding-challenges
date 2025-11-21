from itertools import combinations

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
result=0
for i in range(4):
    xlines=i
    ylines=3-i

    x_list=[j for j in range(min(x), max(x)+1)]
    y_list=[j for j in range(min(y), max(y)+1)]

    x_list=list(combinations(x_list, xlines))
    y_list=list(combinations(y_list, ylines))

    for x_li in x_list:
        for y_li in y_list:
            temp_arr=points[:]
            check=[0]*len(points)
            for j in range(len(points)):
                if points[j][0] in x_li:
                    check[j]=1
                if points[j][1] in y_li:
                    check[j]=1
            if len(check) == sum(check):
                result=1

print(result)
