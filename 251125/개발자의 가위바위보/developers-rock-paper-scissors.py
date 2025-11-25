N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]
a, b = zip(*moves)
a, b = list(a), list(b)

# Please write your code here.

result=0
cnt=0
# Case 1) 가위:1 바위:2 보:3
for move in moves:
    if move == (1,2) or move == (2,3) or move == (3,1):
        cnt+=1
result=max(result, cnt)

cnt=0
# Case 2) 가위:1 바위:3 보:2
for move in moves:
    if move == (1,3) or move == (3,2) or move == (2,1):
        cnt+=1
result=max(result, cnt)

cnt=0
# Case 3) 가위:2 바위:1 보:3
for move in moves:
    if move == (2,1) or move == (13,) or move == (3,2):
        cnt+=1
result=max(result, cnt)

cnt=0
# Case 4) 가위:2 바위:3 보:1
for move in moves:
    if move == (2,3) or move == (3,1) or move == (1,2):
        cnt+=1
result=max(result, cnt)

cnt=0
# Case 5) 가위:3 바위:1 보:2
for move in moves:
    if move == (3,1) or move == (1,2) or move == (2,3):
        cnt+=1
result=max(result, cnt)

cnt=0
# Case 6) 가위:3 바위:2 보:1
for move in moves:
    if move == (3,2) or move == (2,1) or move == (1,3):
        cnt+=1
result=max(result, cnt)

print(result)