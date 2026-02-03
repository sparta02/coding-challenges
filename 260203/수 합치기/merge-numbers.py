n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
result=0

while (len(arr)>1):
    num1=min(arr)
    arr.remove(num1)
    num2=min(arr)
    arr.remove(num2)
    temp_num=num1+num2
    
    arr.append(temp_num)
    result+=temp_num
    #print(arr)

print(result)