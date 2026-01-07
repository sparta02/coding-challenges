import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def move(x, y, w, h):
    #이동방향 x, y, 우상/좌하, 좌상/우하 횟수
    dx=[-1, -1, 1, 1]
    dy=[1, -1, -1, 1]

    moves=[w,h,w,h]

    sum=0
    for i in range(4):
        for _ in range(moves[i]):
            x+=dx[i]
            y+=dy[i]
            if x<0 or x>=n or y<0 or y>=n:
                return 0
            sum+=grid[x][y]
    return sum

def main():
    result=0
    

    for x in range(n):
        for y in range(n):
            for w in range(1,n):
                for h in range(1,n):
                    result= max(result, move(x,y,w,h))
    print(result)


if __name__ == "__main__":
    main()