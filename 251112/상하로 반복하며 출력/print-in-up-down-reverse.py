n=int(input())

arr1=[[0,0,0,0]for _ in range(4)]

for i in range(4):
    cnt=1
    if i%2==0:
        for j in range(4):
            arr1[j][i] = cnt
            cnt+=1
    else:
        for j in range(3,-1,-1):
            arr1[j][i] = cnt
            cnt+=1

for i in range(4):
    for j in range(4):
        print(arr1[i][j],end="")
    print()