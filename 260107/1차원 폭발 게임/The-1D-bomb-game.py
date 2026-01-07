
n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.
# while(1):
while(1):
    start_len=len(numbers)
    n=len(numbers)
    count_index=[0]*len(numbers)
    # print(count_index)
    for i in range(n):
        temp=numbers[i]
        if count_index[i]!=0:
            continue
        count=1

        for j in range(i+1, n):
            if numbers[i] == numbers[j]:
                count+=1
            else:
                break
        # print(i, j, count)
        for j in range(i, i+count):
            count_index[j]=count
    # print(count_index)

    for i in range(n-1,-1,-1):
        
        if count_index[i]>=m:
            # print(i)
            numbers.pop(i)
    # print(numbers)
    end_len=len(numbers)
    
    if start_len==end_len:
        break
print(len(numbers))
for i in range(len(numbers)):
    print(numbers[i])


