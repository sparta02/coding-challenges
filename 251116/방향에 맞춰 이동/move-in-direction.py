n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
pow=[0,0]

for i in range(n):
    if dir[i]=='N':
        pow[1]+=dist[i]
    elif dir[i]=='E':
        pow[0]+=dist[i]
    elif dir[i]=='W':
        pow[0]-=dist[i]
    elif dir[i]=='S':
        pow[1]-=dist[i]

print(pow[0], pow[1])