n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

result=0
for i in range(n-2):
    for j in range(n-2):
        temp=0
        for k in range(i, i+3):
            for l in range(j, j+3):
                #print(k,l)
                temp+=grid[k][l]
        result=max(result, temp)

print(result)
