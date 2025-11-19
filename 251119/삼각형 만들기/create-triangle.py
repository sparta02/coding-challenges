n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
result=0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i==j or j==k or k==i:
                continue
            if x[i]!=x[j] and x[j]!=x[k] and x[k]!=x[i]:
                continue
            if  y[i]!=y[j] and y[j]!=y[k] and y[k]!=y[i]:
                continue
            #print(x[i],y[i], x[j], y[j], x[k], y[k])
            min_x=min(x[i],x[j],x[k])
            min_y=min(y[i],y[j],y[k])
            max_x=max(x[i],x[j],x[k])
            max_y=max(y[i],y[j],y[k])
            result=max(result, (max_x-min_x)*(max_y-min_y))

print(result)