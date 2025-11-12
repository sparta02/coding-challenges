n=int(input())

arr1=[[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    cnt=1
    if i%2==0:
        for j in range(n):
            arr1[j][i] = cnt
            cnt+=1
    else:
        for j in range(n-1,-1,-1):
            arr1[j][i] = cnt
            cnt+=1

for i in range(n):
    for j in range(n):
        print(arr1[i][j],end="")
    print()