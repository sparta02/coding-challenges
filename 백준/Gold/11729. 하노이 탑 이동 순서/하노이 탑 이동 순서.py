n=int(input())


cnt=0

def hanoi(start, mid, end, num):
    global cnt
    if num==1:
        cnt+=1
        return

    hanoi(start, end, mid, num-1)
    cnt+=1
    hanoi(mid, start, end, num-1)

def hanoi2(start, mid, end, num):
    if num==1:
        print(start, end)
        return

    hanoi2(start, end, mid, num-1)
    print(start, end)
    hanoi2(mid, start, end, num-1)


hanoi(1,2,3,n)
print(cnt)
hanoi2(1,2,3,n)