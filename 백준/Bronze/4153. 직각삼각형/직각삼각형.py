a,b,c=1,1,1
while(1):
    a, b, c = map(int, input().split())
    if a==0:
        break
    a2=a*a
    b2=b*b
    c2=c*c
    if a2+b2==c2 or a2+c2==b2 or b2+c2==a2:
        print("right")
    else:
        print("wrong")