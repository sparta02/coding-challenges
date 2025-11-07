a,b,c = map(int, input().split())

if a<b<c or c<b<a:
    print(b)
elif a<c<b or b<c<a:
    print(c)
else:
    print(a)