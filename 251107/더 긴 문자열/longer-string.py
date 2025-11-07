a,b= input().split()
c=len(a)
d=len(b)
if c>d:
    print(a, end=" ")
    print(c)
elif d>c:
    print(b, end=" ")
    print(d)
else:
    print('same')