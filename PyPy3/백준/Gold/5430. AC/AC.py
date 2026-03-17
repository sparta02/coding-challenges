from collections import deque
t= int(input())


for _ in range(t):
    p=list(input())
    count_D=p.count('D')

    n=int(input())

    arr=list(input())
    arr=arr[1:-1]
    arr=list("".join(arr).split(','))
    # print(arr)
    # queue=deque()
    # for i in arr[::2]:
    #     queue.append(i)
    # 배열이 비어있는데 D를 사용하는 경우
    if n<count_D:
        print('error')
        continue
    
    # 최종적으로 출력할 범위 [start:end]
    start=0
    end=n-1
    # flag: 0이면 정방향, 1이면 역방향
    flag=0

    for com in p:
        if com=='R':
            flag=(flag+1)%2
        else:
            if flag==0:
                start+=1
            else:
                end-=1

    print("[", end="")
    temp_arr=arr[start:end+1]
    if flag==1:
        temp_arr=temp_arr[::-1]
    for i in range(len(temp_arr)):
        if i!=len(temp_arr)-1:
            print(temp_arr[i], end=",")
        else:
            print(temp_arr[i], end="")

    print("]")    


    