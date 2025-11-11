a3=0
a5=0

for i in range(10):
    n=int(input())
    if n%3==0:
        a3+=1
    if n%5==0:
        a5+=1
print(f"{a3} {a5}")