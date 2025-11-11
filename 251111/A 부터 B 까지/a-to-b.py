a,b = map(int, input().split())

while True:
    print(a, end=" ")
    if a%2==0:
        a+=3
    else:
        a*=2
    if a>b:
        break