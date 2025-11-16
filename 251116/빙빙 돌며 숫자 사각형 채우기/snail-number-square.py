n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.

dxs, dys=[0,1,0,-1], [1,0,-1,0]

arr[0][0]=1
way=0

x=0
y=0

def check(a, b):
    if 0<=a<n and 0<=b<m:
        return True
    return False

def pri():
    global arr
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print()
    print()

for i in range(2, n*m+1):
    if check(x+dxs[way], y+dys[way])==False or arr[x+dxs[way]][y+dys[way]]!=0:
        way=(way+1)%4
        
    arr[x+dxs[way]][y+dys[way]]=i
    x+=dxs[way]
    y+=dys[way]
pri()


    