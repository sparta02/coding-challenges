n=int(input())
points=[]

for _ in range(n):
    x,y = map(int, input().split())
    points.append((x,y))
points.append(points[0])
result=0
for i in range(n):
    result+=points[i][0]*points[i+1][1]
    result-=points[i][1]*points[i+1][0]
print(f"{abs(result/2):.1f}")