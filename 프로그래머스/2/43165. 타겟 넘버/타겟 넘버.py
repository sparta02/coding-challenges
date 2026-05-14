selected=[]
n=200
answer = 0

def calc(numbers,target):
    global answer
    temp=0
    for i in range(n):
        temp+=(-1 if selected[i]=='-' else 1)*numbers[i]
    if temp==target:
        answer+=1

def choose(cnt,numbers,target):
    if len(selected)==n:
        calc(numbers,target)
        return
    selected.append('+')
    choose(cnt+1,numbers,target)
    selected.pop()
    selected.append('-')
    choose(cnt+1,numbers,target)
    selected.pop()

def solution(numbers, target):
    global n
    
    n=len(numbers)
    
    choose(0,numbers,target)
    
    return answer