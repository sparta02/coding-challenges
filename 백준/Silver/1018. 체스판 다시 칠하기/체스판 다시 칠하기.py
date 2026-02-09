n, m = map(int, input().split())
board= [input() for _ in range(n)]
기준1=[
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]

기준2=[
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
]

def count_paint1(x, y):
    cnt=0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if 기준1[i-x][j-y] != board[i][j]:
                cnt+=1
    return cnt

def count_paint2(x, y):
    cnt=0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if 기준2[i-x][j-y] != board[i][j]:
                cnt+=1
    return cnt


result=999999
for x in range(n-7):
    for y in range(m-7):
        result=min(result, count_paint1(x, y))
        result=min(result, count_paint2(x, y))
print(result)