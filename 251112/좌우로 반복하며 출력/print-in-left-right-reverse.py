a= int(input())

for i in range(a):
    if i%2==0:
        for j in range(1, a+1):
            print(j,end="")
    else:
        for j in range(a, 0, -1):
            print(j,end="")
    print()