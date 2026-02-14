n, m= map(int, input().split())

select=[]
grid= [ list(map(int, input().split())) for _ in range(n)]

# 치킨집 목록
chicken=[]

# 가정집 목록
house=[]

for i in range(n):
        for j in range(n):
            if grid[i][j]==1:
                house.append((i,j))
            if grid[i][j]==2:
                chicken.append((i,j))


def print_grid(grid):
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print()
    print()


result=10**9

def calc():
    global result
    chicken_dist=0

    for x,y in house:
        temp=10**9
        for i in select:
            temp=min(temp, abs(x-chicken[i][0])+abs(y-chicken[i][1]))
        #print(x, y, temp)
        chicken_dist+=temp
    #print(chicken_dist)
    result=min(result, chicken_dist)



def choose(start_num, k):
    if k==m:
        #print(select)
        calc()
        return
    
    for i in range(start_num, len(chicken)):
        select.append(i)
        choose(i+1, k+1)
        select.pop()

choose(0,0)

print(result)