cnt=0

queen=[-1]

def okay(i):
    if i in queen:
        return False
    len_list=len(queen)
    for j in range(1, len(queen)):
        if len_list-j == abs(i-queen[j]):
            return False
    return True

def calc(n, curr):
    global cnt
    if curr==n+1:
        cnt+=1
        # print(queen[1:])
        return
        
    if curr==1:
        for i in range(1, n+1):
            queen.append(i)
            calc(n, curr+1)
            queen.pop()
    else:
        for i in range(1, n+1):
            if okay(i):
                queen.append(i)
                calc(n, curr+1)
                queen.pop()

def solution(n):
    calc(n, 1)
    

    return cnt