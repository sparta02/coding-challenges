import sys

n, m, t = map(int, input().split())

balls=[]
for i in range(m):
    ri, ci, di, wi = input().split()
    temp_list=[]
    temp_list.append(int(ri)-1)
    temp_list.append(int(ci)-1)
    if di=="U":
        temp_list.append(0)
    elif di=="R":
        temp_list.append(1)
    elif di=="D":
        temp_list.append(2)
    elif di=="L":
        temp_list.append(3)
    temp_list.append(int(wi))
    temp_list.append(i)
    balls.append(temp_list)

# Please write your code here.
#print(balls)

# 위, 오른쪽, 아래, 왼쪽
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def move(x, y, way):
    if not (0<=x+dx[way]<n and 0<=y+dy[way]<n):
        way =(way+2)%4
    else:
        x+=dx[way]
        y+=dy[way]
    return (x, y, way)

def main():
    global balls
    for time in range(t):
        grid=[ [[] for _ in range(n)]
                for _ in range(n)]
        
        for i in range(len(balls)):
            balls[i][0], balls[i][1], balls[i][2] = move(balls[i][0], balls[i][1], balls[i][2])
            grid[balls[i][0]][balls[i][1]].append([balls[i][2], balls[i][3], balls[i][4]])
        #print(grid)
        new_balls=[]

        for i in range(n):
            for j in range(n):
                if len(grid[i][j])==1:
                    new_balls.append([i,j,grid[i][j][0][0],grid[i][j][0][1],grid[i][j][0][2]])
                elif len(grid[i][j])>1:
                    temp_list=grid[i][j]
                    temp_list=sorted(temp_list, key=lambda x: -x[1])

                    temp_sum=0
                    for k in range(len(temp_list)):
                        temp_sum+=temp_list[k][1]
                    temp_list[0][1]=temp_sum
                    new_balls.append([i,j,temp_list[0][0],temp_list[0][1],temp_list[0][2]])
                    #print(temp_sum)
        #print(new_balls)
        balls=new_balls

    print(len(balls), max([ x[3] for x in balls ]))

if __name__=="__main__":
    main()

