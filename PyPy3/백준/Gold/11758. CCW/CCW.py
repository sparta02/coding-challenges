import sys
a1,a2=map(int, input().split())
b1,b2=map(int, input().split())
c1,c2=map(int, input().split())

# CASE 1. 수직 (위에서 아래)
if a1==b1 and a2>b2:
    if c1<a1:
        print(-1)
    elif c1>a1:
        print(1)
    else:
        print(0)
# CASE 2. 수직 (아래에서 위)     
elif a1==b1 and a2<b2:
    if c1<a1:
        print(1)
    elif c1>a1:
        print(-1)
    else:
        print(0)
# CASE 3. 세 점이 일직선
elif (b2-a2)*(c1-b1)==(c2-b2)*(b1-a1):
    print(0)
    sys.exit()
# CASE 3. 왼쪽 -> 오른쪽
elif a1<b1:
    # y=nx+m
    n=(b2-a2)/(b1-a1)
    m=a2-n*a1
    # f(x,y)= y-nx-m
    temp=c2-n*c1-m
    if temp>0:
        print(1)
    elif temp<0:
        print(-1)
# CASE 4. 오른쪽 -> 왼쪽
else:
    # y=nx+m
    n=(b2-a2)/(b1-a1)
    m=a2-n*a1
    # f(x,y)= y-nx-m
    temp=c2-n*c1-m
    if temp>0:
        print(-1)
    elif temp<0:
        print(1)
