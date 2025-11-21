n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x=[p[0] for p in points]
y=[p[1] for p in points]

# Please write your code here.
result=9999999999999999999
min_x= min(x)
min_y= min(y)
max_x=max(x)
max_y=max(y)

for i in range(min_x+1, max_x,2):
    for j in range(min_y+1, max_y,2):
        일사분면=0
        이사분면=0
        삼사분면=0
        사사분면=0
        for point in points:
            if point[0]>i:
                if point[1]>j:
                    일사분면+=1
                else:
                    사사분면+=1
            else:
                if point[1]>j:
                    이사분면+=1
                else:
                    삼사분면+=1
        최대개수=max(일사분면,이사분면,삼사분면,사사분면)
        result=min(result, 최대개수)
print(result)