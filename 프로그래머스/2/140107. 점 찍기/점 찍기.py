def pitagoras(a,b,c):
    if c*c>=a*a+b*b:
        return True
    return False

def solution(k, d):
    answer = 0
    endpoint=k*(d//k)
    #x=0~endpoint
    #y= endpoint~0
    y=endpoint
    for x in range(0, endpoint+1, k):
        while pitagoras(x, y, d)==False:
            y-=k
        answer+=(y//k)+1
    
    return answer
