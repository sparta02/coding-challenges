n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
def calc(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)

min=99999999999999999999999999999

for i in range(1, n-1):
    x1=0
    y1=0
    x2=1
    y2=1
    sum=0
    for j in range(1, n-1):
        #print(f"실행 전 i:{i} j:{j} x1:{x1}, y1:{y1}, x2:{x2},y2:{y2}")
        if i==j:
            x2+=1
            y2+=1
        #print(f"중간 i:{i} j:{j} x1:{x1}, y1:{y1}, x2:{x2},y2:{y2}")
        sum+=calc(x[x1], y[y1], x[x2], y[y2])
        x1+=1
        y1+=1
        x2+=1
        y2+=1
        if i==j:
            x1+=1
            y1+=1
        
        #print(f"실행 후 i:{i} j:{j} x1:{x1}, y1:{y1}, x2:{x2},y2:{y2}, sum:{sum}")
    if min>sum:
        min=sum
    #print()

print(min)

