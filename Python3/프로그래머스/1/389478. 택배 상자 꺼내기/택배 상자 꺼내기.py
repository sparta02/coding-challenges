def solution(n, w, num):
    answer = 0
    
    x_length=w
    y_length=(n+w-1)//w
    
    arr=[ [0]*x_length for _ in range(y_length)]
    
    for i in range(y_length):
        for j in range(x_length):
            if i%2==0:
                temp=(w*i+j)+1
            else:
                temp=(i+1)*w-j
            if temp<=n:
                arr[i][j]=temp
    
    print(arr)
    where_x=0
    where_y=0
    
    for i in range(y_length):
        for j in range(x_length):
            if arr[i][j]==num:
                where_x=i
                where_y=j
    print(where_x, where_y)
    
    result=1
    for j in range(where_x+1, y_length): # y값
        if arr[j][where_y]!=0:
            result+=1
            
    return result
