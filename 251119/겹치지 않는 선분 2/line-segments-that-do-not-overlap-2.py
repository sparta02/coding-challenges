n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
result=[0]*n

# Please write your code here.

cnt=0
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        if lines[i][0]<lines[j][0]<lines[i][1] and lines[i][0]<lines[j][1]<lines[i][1]:
            result[i]=1
            result[j]=1

print(sum(result))