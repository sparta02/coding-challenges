commands = input()

# Please write your code here.

dxs, dys = [0,1,0,-1],[1,0,-1,0]
x=0
y=0
way=0
cnt=0
for com in commands:
    cnt+=1
    if com=='F':
        x+=dxs[way]
        y+=dys[way]
    elif com=='L':
        way=(way+3)%4
    elif com=='R':
        way=(way+1)%4
    # 검사
    if x==0 and y==0:
        print(cnt)
        break
else:
    print(-1)
