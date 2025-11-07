a,b,c = map(int, input().split())

if a<b and b<c:
    print(b)
elif a<c and c<b:
    print(c)
else:
    print(a)