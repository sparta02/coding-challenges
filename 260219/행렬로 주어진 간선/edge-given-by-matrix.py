n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result=[ row[:] for row in graph]
# Please write your code here.

for i in range(n):
    result[i][i]=1

def print_result():
    for i in range(n):
        for j in range(n):
            print(result[i][j], end=" ")
        print()
    print()

for k in range(n):
    for i in range(n):
        for j in range(n):
            result[i][j]= (1 if result[i][k] and result[k][j] else result[i][j])

print_result()
