n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
result=[0]*n

# Please write your code here.

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        if (lines[i][0]<lines[j][0] and lines[j][1]<lines[i][1]) or (lines[i][0]>lines[j][0] and lines[j][1]>lines[i][1]):
            result[i]=1
            result[j]=1

print(n-sum(result))