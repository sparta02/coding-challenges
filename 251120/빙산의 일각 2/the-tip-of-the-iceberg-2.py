n = int(input())
h = [int(input()) for _ in range(n)]

# Please write your code here.
result=0
for i in range(max(h)):
    temp_arr=h[:]
    for j in range(n):
        temp_arr[j]-=i

    #print(temp_arr)
    sum=0
    wait=1
    for j in range(n):
        
        if temp_arr[j]>0 and wait==1:
            sum+=1
            wait=0
        elif temp_arr[j]<=0:
            wait=1
        #print(temp_arr[j], sum ,wait)
    result=max(result, sum)
print(result)