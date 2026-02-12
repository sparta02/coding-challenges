n=int(input())
row=[-999999]*n
result=0

def check_queen(x):
    for i in range(x):
        # i, row[i]에 있는 퀸과
        # x, row[x]에 있는 퀸 비교
        if abs(i-x)==abs(row[i]-row[x]):
            return False
    return True



def queen(num):
    global result
    if num==n:
        result+=1
        return
    #print(f"num:{num}")
    for i in range(n):
        if i in row:
            continue
        row[num]=i
        if check_queen(num):
            #print(f"add {i}")
            queen(num+1)
        row[num]=-999999

queen(0)
print(result)