n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
result=0

#Case 1. 오른쪽 위로 가는 사각형
# grid[i][0]에서 맨 위, 맨 아래만 제외하고 시작점으로 설정
for i in range(1, n-1):
    #i는 1, 2, 3
    temp=0
    x=i
    y=0
    for j in range(i+1):
        #j는 2회, 3회, 4회
        temp+=grid[x][y]
        temp+=grid[x+1][y+1]
        x-=1
        y+=1
    #print(temp)
    result =max(result, temp)
#print()

#Case 2. 오른쪽 위로 가는 사각형
# grid[n-1][i]에서 맨 앞, 맨 끝만 제외하고 시작점으로 설정
for i in range(1, n-1):
    #i는 1, 2, 3
    temp=0
    x=n-1
    y=i
    for j in range(n-i,0,-1):
        #j는 4회, 3회, 2회
        temp+=grid[x][y]
        temp+=grid[x-1][y-1]
        x-=1
        y+=1
    #print(temp)
    result =max(result, temp)
#print()

#Case 3. 오른쪽 아래로 가는 사각형
# grid[0][i]에서 맨 위, 맨 아래만 제외하고 시작점으로 설정
for i in range(1, n-1):
    #i는 1, 2, 3
    temp=0
    x=0
    y=i
    for j in range(n-i,0,-1):
        #j는 4회, 3회, 2회
        temp+=grid[x][y]
        temp+=grid[x+1][y-1]
        x+=1
        y+=1
    #print(temp)
    result =max(result, temp)
#print()

#Case 4. 오른쪽 아래로 가는 사각형
# grid[i][0]에서 맨 위, 맨 아래만 제외하고 시작점으로 설정
for i in range(1, n-1):
    #i는 1, 2, 3
    temp=0
    x=i
    y=0
    for j in range(n-i,0,-1):
        #j는 2회, 3회, 4회
        temp+=grid[x][y]
        temp+=grid[x-1][y+1]
        x+=1
        y+=1
    #print(temp)
    result =max(result, temp)
# print()

print(result)