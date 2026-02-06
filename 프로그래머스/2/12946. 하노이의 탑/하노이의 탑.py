def hanoi (a, b, c, n, answer):
    if n==1:
        #print(a, c)
        answer.append([a, c])
        return
        
    else:
        hanoi(a, c, b, n-1, answer)
       # print(a, c)
        answer.append([a, c])
        hanoi(b, a, c, n-1, answer)
        

def solution(n):
    answer = []
    hanoi(1, 2, 3, n, answer)
    return answer