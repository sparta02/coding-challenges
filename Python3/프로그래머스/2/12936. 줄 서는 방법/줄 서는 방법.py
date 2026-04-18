def fact(num):
    temp=1
    for i in range(1, num+1):
        temp*=i
    return temp

def calc_idx(remain, curr, dist):
    # if dist==1:
    #     return 0
    # elif dist==2:
    #     if curr==1:
            
    return curr//(fact(dist-1))

def solution(n, k):
    result=[]
    k-=1
    remain=[i for i in range(1, n+1)]
    for i in range(n,0,-1):
        temp_idx=calc_idx(remain, k, i)
        # print(temp_idx)
        result.append(remain.pop(temp_idx))
        k%=(fact(i-1))
        # print(remain, k)
    return result
