n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

# Please write your code here.

result=0
for i in range(n):
    arr=[0]*(n+1)
    arr[i]=1
    cnt=0
    for move in moves:
        arr[move[0]], arr[move[1]]=arr[move[1]], arr[move[0]]
        if arr[move[2]]==1:
            cnt+=1
    result=max(result, cnt)

print(result)
