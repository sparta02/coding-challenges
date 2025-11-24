n = int(input())
adjacent = list(map(int, input().split()))

# Please write your code here.
arr=[i for i in range(1, n+1)]

for i in range(1, n+1):
    temp_arr=[]
    temp_arr.append(i)

    check_list=[0]*(n+1)
    check_list[i]=1
    #print(temp_arr, check_list)
    for j in range(n-1):
        #print(adjacent[j], temp_arr[-1])
        next_num=adjacent[j]-temp_arr[-1]
        #print(temp_arr, check_list, next_num)
        if next_num > n or next_num<1 or check_list[next_num]==1:
            break
        else:
            check_list[next_num]=1
            temp_arr.append(next_num)
            if len(temp_arr)==n:
                for k in range(n):
                    print(temp_arr[k], end=" ")