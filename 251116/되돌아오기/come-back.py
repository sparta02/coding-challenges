N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

dxs, dys=[1,0,-1,0], [0,-1,0,1]
x=0
y=0

ways={
    "N":3,
    "E":0,
    "W":2,
    "S":1
}
result=-1
아=0
cnt=0
for i in range(N):
    for j in range(dist[i]):
        x+=dxs[ways.get(dir[i])]
        y+=dys[ways.get(dir[i])]
        cnt+=1

        if x==0 and y==0:
            print(cnt)
            아=1
            break
if 아==0:
    print(-1)
    