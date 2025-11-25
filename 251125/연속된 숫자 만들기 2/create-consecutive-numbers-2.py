a,b,c = list(map(int, input().split()))

# Please write your code here.
A=abs(a-b)
B=abs(b-c)
C=abs(c-a)

if (A+B==2 or B+C==2 or A+C==2):
    print(0)
elif A==2 or B==2 or C==2:
    print(1)
else:
    print(2)