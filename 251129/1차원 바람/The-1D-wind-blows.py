n, m, q = map(int, input().split())
winds = [list(map(int, input().split())) for _ in range(n)]
a = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

# Please write your code here.
def push_left(num):
    global winds
    temp=winds[num][0]
    for i in range(m-1):
        winds[num][i]=winds[num][i+1]
    winds[num][m-1]=temp


def push_right(num):
    global winds
    temp=winds[num][m-1]
    for i in range(m-1):
        winds[num][m-i-1]=winds[num][m-i-2]
    winds[num][0]=temp

def print_arr():
    for i in range(n):
        for j in range(m):
            print(winds[i][j], end=" ")
        print()

def check_push(current, new):
    # print(f"current={current}, new={new}")
    for i in range(m):
        # print(winds[current][i], winds[new][i])
        if winds[current][i] == winds[new][i]:
            return True
    return False

for inst in a:
    up_way=0
    up_current=inst[0]-1

    down_way=0
    down_current=inst[0]-1
    # print(up_current)
    # print_arr()
    # print()

    if inst[1] =="R":
        push_left(up_current)
        up_way=1
        down_way=1
    else:
        push_right(up_current)
        up_way=0
        down_way=0

    # print_arr()
    # print()
    
    while(1):
        up_current-=1
        if up_current<0 or not check_push(up_current, up_current+1):
            break
        if up_way == 0:
            push_left(up_current)
            up_way=1
        else:
            push_right(up_current)
            up_way=0
    
    while(1):
        down_current+=1
        if down_current>=n or not check_push(down_current, down_current-1):
            break
        if down_way == 0:
            push_left(down_current)
            down_way=1
        else:
            push_right(down_current)
            down_way=0
    # print_arr()
    # print()


print_arr()