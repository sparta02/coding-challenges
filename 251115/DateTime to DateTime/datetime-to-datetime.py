a, b, c = map(int, input().split())

# Please write your code here.
n1=11+11*60+11*1440
n2=c+b*60+a*1440

if n1>n2:
    print(-1)
else:
    print(n2-n1)