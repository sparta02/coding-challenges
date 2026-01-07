import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
x, y, m1, m2, m3, m4, dir = map(int, input().split())


def print_grid():
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print()
    print()

# Please write your code here.
def not_clock_way(x,y,m1,m2,dir):
    if dir==0:
        dx=[-1,-1,1,1]
        dy=[1,-1,-1,1]
        moves=[m1,m2,m1,m2]
    else:
        dx=[-1,-1,1,1]
        dy=[-1,1,1,-1]
        moves=[m2,m1,m2,m1]
    

    next_num=grid[x][y]
    for i in range(4):
        for _ in range(moves[i]):
            next_x=x+dx[i]
            next_y=y+dy[i]

            #print(f"next_x:{next_x}, next_y:{next_y}, x:{x}, y:{y}")
            #print(f"grid[next_x][next_y]:{grid[next_x][next_y]}, grid[x][y]:{grid[x][y]}")

            next_temp=grid[next_x][next_y]
            grid[next_x][next_y]=next_num
            next_num=next_temp

            x+=dx[i]
            y+=dy[i]
            #print_grid()
    print_grid()
    
    

def main():
    not_clock_way(x-1,y-1,m1,m2,dir)

if __name__ == "__main__":
    main()