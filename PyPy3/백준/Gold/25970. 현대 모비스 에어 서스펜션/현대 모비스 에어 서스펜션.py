import sys
input=sys.stdin.readline

b= int(input())
down_bit=[ input().strip() for _ in range(b)]
up_bit=[ input().strip() for _ in range(b)]

n=int(input())
arr=[ input().strip() for _ in range(n)]

def find_cnt(bit, target):
    cnt=0
    start=0
    while True:
        idx=bit.find(target, start)
        if idx==-1:
            break
        cnt+=1
        start=idx+1
    return cnt
    

for bit in arr:
    down_cnt=0
    up_cnt=0
    for target in down_bit:
        down_cnt+=find_cnt(bit, target)
    for target in up_bit:
        up_cnt+=find_cnt(bit, target)
    if down_cnt==up_cnt:
        print('GOOD')
    elif down_cnt>up_cnt:
        print(f"HIGH {down_cnt-up_cnt}")
    else:
        print(f"LOW {up_cnt-down_cnt}")

