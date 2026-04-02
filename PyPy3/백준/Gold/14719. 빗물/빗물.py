n, m = map(int, input().split())
grid=list(map(int, input().split()))

def check(x, y):
    flag1=0
    flag2=0
    # 왼쪽 체크
    for i in range(y-1, -1, -1):
        if n-x<=grid[i]:
            flag1=1
            break
    # 오른쪽 체크
    for i in range(y+1, m):
        if n-x<=grid[i]:
            flag2=1
            break
    
    if flag1 and flag2:
        # print(x, y)
        return True
    return False 

result=0

for i in range(n):
    for j in range(m):
        if n-i>grid[j]:
            if check(i,j):
                result+=1
print(result)