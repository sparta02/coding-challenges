n, T = map(int, input().split())
str = input()
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def check(x, y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

x=int(n/2)
y=int(n/2)
way=0
dx, dy= [-1,0,1,0], [0,1,0,-1]

sum=arr[x][y]

for st in str:
    if st=='R':
        way=(way+1)%4
    elif st=='L':
        way=(way+3)%4
    elif st=='F':
        if check(x+dx[way], y+dy[way]) == False:
            continue
        x+=dx[way]
        y+=dy[way]
        sum+=arr[x][y]
    #print(x, y, way, arr[x][y], sum)
print(sum)