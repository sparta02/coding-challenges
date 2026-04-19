def solution(n,a,b):
    answer = 1

    a, b=min(a,b), max(a,b)
    while True:
        if int(a/2+0.5)==int(b/2+0.5):
            break
        else:
            answer+=1
            a=int(a/2+0.5)
            b=int(b/2+0.5)

    return answer

# 1 2 3 4 5 6 7 8
# 0.5 1 1.5 2
# 1 