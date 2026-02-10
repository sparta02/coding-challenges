n, r, c = map(int, input().split())

# x, y: 시작 지점
# r, c: 찾는 지점
def find(x,y,r,c,n):
    # print(f"start from {x}, {y}")
    # print(f"looking for {r}, {c}")
    # print(f"n:{n}")
    if n==1:
        return 1
    if n==2:
        if x==r and y==c:
            return 1
        elif x==r and y+1==c:
            return 2
        elif x+1==r and y==c:
            return 3
        elif x+1==r and y+1==c:
            return 4
    # 왼쪽 위에 있는 경우
    if x<=r<x+int(n/2) and y<=c<y+int(n/2):
        #print("case 1")
        return find(x,y,r,c,int(n/2))
    # 왼쪽 아래
    elif x+int(n/2)<=r<x+n and y<=c<y+int(n/2):
        #print("case 2")
        return int(n*n/2)+find(x+int(n/2),y,r,c,int(n/2))
    # 오른쪽 위
    elif x<=r<x+int(n/2) and y+int(n/2)<=c<y+n:
        #print("case 3")
        return int(n*n/4)+find(x,y+int(n/2),r,c,int(n/2))
    # 오른쪽 아래
    elif x+int(n/2)<=r<x+n and y+int(n/2)<=c<y+n:
        #print("case 4")
        return int(n*n/4*3)+find(x+int(n/2),y+int(n/2),r,c,int(n/2))

print(find(0,0,r,c,2**n)-1)
