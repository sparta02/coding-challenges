from collections import deque
t=int(input())

def D(num):
    return num*2%10000

def S(num):
    return num-1 if num!=0 else 9999

def L(num):
    # 1234 -> 2341
    d1=int(num/1000)
    num=(num*10)%10000+d1
    return num

def R(num):
    # 1234 -> 4123
    d4=num%10
    return int(num/10)+d4*1000

for _ in range(t):
    
    A, B = map(int, input().split())
    visited=[0]*10000
    queue=deque()
    queue.append((A, ''))
    visited[A]=1


    while queue:
        curr_num, curr_com=queue.popleft()
        if curr_num==B:
            print(curr_com)
            break
        
        temp=D(curr_num)
        if visited[temp]==0:
            queue.append((temp, curr_com+'D'))
            visited[temp]=1

        temp=S(curr_num)
        if visited[temp]==0:
            queue.append((temp, curr_com+'S'))
            visited[temp]=1

        temp=R(curr_num)
        if visited[temp]==0:
            queue.append((temp, curr_com+'R'))
            visited[temp]=1

        temp=L(curr_num)
        if visited[temp]==0:
            queue.append((temp, curr_com+'L'))
            visited[temp]=1
        






